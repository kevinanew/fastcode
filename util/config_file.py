import os
import shutil

import yaml


def load_config(filename):
    yaml_file = open(os.path.join(os.getcwd(), filename), 'r')
    yaml_content = yaml.safe_load(yaml_file)
    return yaml_content


def build_config(filename):
    config_template = os.path.join(os.path.dirname(__file__), filename)

    if not os.path.exists(config_template):
        print(f'配置模版不存在: {config_template}')
        raise SystemExit

    config_path = os.path.join(os.getcwd(), filename)
    if not os.path.exists(config_path):
        print(f'创建配置文件: {filename}')
        shutil.copy(config_template, config_path)


if __name__ == '__main__':
    load_config('fapi.yaml')
