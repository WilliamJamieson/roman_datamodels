from re import I
from numpy import isin
import roman_datamodels as rdm
import roman_datamodels.stnode as stnode

def extract_schema_data(data_key, node, schema):
    schema_data = {}
    for key, data in schema.items():
        if isinstance(data, dict):
            if data_key in data:
                schema_data[key] = (data[data_key], getattr(node, key))
    
    return schema_data


def extract_tagged_node_data(data_key, node):
    if (schema := node.get_schema().get('properties', None)) is not None:
        return extract_schema_data(data_key, node, schema)


def extract_dnode_data(data_key, dnode):
    data = {}
    for key, node in dnode.items():
        if isinstance(node, stnode.TaggedObjectNode):
            data[key] = extract_tagged_node_data(data_key, node)

    return data


def extract_nodes(model):
    nodes = {}
    for key in model.keys():
        node = getattr(model, key)

        if isinstance(node, stnode.DNode):
            nodes[key] = node

    return nodes

def extract_data(data_key, filename):
    model = rdm.open(filename)
    nodes = extract_nodes(model)

    data = {}
    for key, node in nodes.items():
        data[key] = extract_dnode_data(data_key, node)

    return data


if __name__ == "__main__":
    filename = "../r0000101001001001001_01101_0001_WFI01_cal.asdf"

    data = extract_data("archive_catalog", filename)
    try:
        from flatten_dict import flatten

        print(flatten(data, "dot"))
    except ImportError:
        print(data)