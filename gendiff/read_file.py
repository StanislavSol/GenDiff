import yaml
import json
import os


def get_read_file(data, extension):
     if extension == '.json':
         return json.loads(data)
     elif extension in ('.yml', '.yaml'):
         return yaml.safe_load(data)


def get_decoder_data(file_path):
    with open(file_path) as data:
        _, extension = os.path.splitext(file_path)
        read_file = data.read()
    return get_read_file(read_file, extension) 
