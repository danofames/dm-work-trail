import yaml

def write_in_yaml(data):
    return yaml.dump(data, default_flow_style=False)
