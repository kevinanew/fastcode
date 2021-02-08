import os

import yaml


def load_config(filename):
    os.getcwd()
    yaml_file = open(os.path.join(os.getcwd(), filename), 'r')
    yaml_content = yaml.safe_load(yaml_file)
    return yaml_content


if __name__ == '__main__':
    load_config('fapi.yaml')
