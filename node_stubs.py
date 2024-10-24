from roman_datamodels.datamodels import MODEL_REGISTRY
from roman_datamodels.maker_utils import mk_datamodel, mk_node
from roman_datamodels.stnode import NODE_CLASSES

for name, model in MODEL_REGISTRY.items():
    print(f"Creating {name} model to read types")
    mk_datamodel(model)

for node_class in NODE_CLASSES:
    print(f"Creating {node_class.__name__} node to read types")
    mk_node(node_class)
