from pathlib import Path

from roman_datamodels.stnode import nodes
from roman_datamodels.stnode._tagged import TaggedListNode, TaggedScalarNode

stub_path = Path(nodes.__file__).parent / "nodes.pyi"
assert stub_path.exists()

with open(stub_path) as f:
    lines = f.readlines()

new_file = [
    "from __future__ import annotations\n",
    "from typing import Any\n",
    "import numpy as np\n",
]
current_class = None
for line in lines:
    if line.strip().startswith("_"):
        continue

    if "class" in line:
        current_class = getattr(nodes, line.split("(")[0].split(" ")[1])

        if issubclass(current_class, (TaggedListNode, TaggedScalarNode)):
            new_file.append(f"{line.strip()} ...\n")
        else:
            new_file.append(line)
        continue

    if current_class is not None and line.strip():
        if isinstance(getattr(current_class, line.split(":")[0].strip()), property):
            entry = f"{line.split(':')[0].strip()}"
            entry_type = current_class.__annotations__[entry]
            entry_type_name = ""
            if entry_type.__module__ == "builtins":
                entry_type_name = entry_type.__name__
            elif entry_type.__module__ == "numpy":
                entry_type_name = f"np.{entry_type.__name__}"
            elif entry_type.__module__ == "typing":
                entry_type_name = entry_type.__name__
            elif entry_type.__module__ == nodes.__name__:
                entry_type_name = entry_type.__name__
            else:
                entry_type_name = f"{entry_type.__module__}.{entry_type.__name__}"

            new_file.append("    @property\n")
            new_file.append(f"    def {entry}(self) -> {entry_type_name}: ...\n")
            new_file.append(f"    @{entry}.setter\n")
            new_file.append(f"    def {entry}(self, value: {entry_type_name}) -> None: ...\n")
            continue

    new_file.append(line)

with open(stub_path, "w") as f:
    f.writelines(new_file)
