#!/usr/bin/env python3
import yaml
import json


KEY_INDEX_IN_TUPLE = 0
LAST_ELEMENT_FILE_NAME = -1
THIRD_KEY_CHAR = 2


def get_first_char_if_the_key(value):
    return value[KEY_INDEX_IN_TUPLE][THIRD_KEY_CHAR:]


def get_difference_dict(data1, data2):
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        if key not in data1:
            result['+ ' + key] = data2[key]
        elif key not in data2:
            result['- ' + key] = data1[key]
        elif data1[key] == data2[key]:
            result['  ' + key] = data1[key]
        else:
            if isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result['  ' + key] = get_difference_dict(data1[key],
                                                         data2[key])
            else:
                result['- ' + key] = data1[key]
                result['+ ' + key] = data2[key]

    result = sorted(result.items(), key=get_first_char_if_the_key)
    return dict(result)


def get_decoder_data(file_path1, file_path2):
    if file_path1.split('.')[LAST_ELEMENT_FILE_NAME] in ('yaml', 'yml'):
        with open(file_path1) as data1, open(file_path2) as data2:
            file1 = yaml.safe_load(data1)
            file2 = yaml.safe_load(data2)
    else:
        with open(file_path1) as data1, open(file_path2) as data2:
            file1 = json.load(data1)
            file2 = json.load(data2)

    return get_difference_dict(file1, file2)
