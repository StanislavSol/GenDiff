import yaml
import json
import os


def get_decoder_data(file_path):
    with open(file_path) as data:
        _, extension = os.path.splitext(file_path)
        if extension == '.json':
            return json.load(data)
        elif extension in ('.yml', '.yaml'):
            return yaml.safe_load(data)
