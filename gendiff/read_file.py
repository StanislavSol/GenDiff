import yaml
import json
import os


def get_decoder_data(file_path):
    with open(file_path) as data:
        if '.json' in os.path.splitext(file_path):
            return json.load(data)
        else:
            return yaml.safe_load(data)
