#!/usr/bin/env python3
import yaml
import json


LAST_ELEMENT_FILE_NAME = -1


def get_decoder_data(file_path1, file_path2):
    file_format = file_path1.split('.')[LAST_ELEMENT_FILE_NAME]
    with open(file_path1) as data1, open(file_path2) as data2:
        if file_format == 'json':
            return json.load(data1), json.load(data2)
        else:
            return yaml.safe_load(data1), yaml.safe_load(data2)
