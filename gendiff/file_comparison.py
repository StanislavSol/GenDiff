import json
import yaml
from itertools import chain


def stylish(value, replacer=' ', spaces_count=4):
    def iter_(current_value, depth=0):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if key[0] in (' ', '+', '-'):
                lines.append(f'{deep_indent[2:]}{key}: {iter_(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = chain('{', lines, [current_indent + '}'])
        result = map(lambda string: string.lower(), result)
        return '\n'.join(result)
    return iter_(value)


def diff(data1, data2):
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
                result['  ' + key] = diff(data1[key], data2[key])
            else:
                result['- ' + key] = data1[key]
                result['+ ' + key] = data2[key]

    result = dict(sorted(result.items(), key=lambda string: string[0][2:]))
    return result
    

def generate_diff(file_path1, file_path2):
    if file_path1.split('.')[-1] in ('yaml', 'yml'):
        with open(file_path1) as data1, open(file_path2) as data2:
            file1 = yaml.safe_load(data1)
            file2 = yaml.safe_load(data2)
    else:
        with open(file_path1) as data1, open(file_path2) as data2:
            file1 = json.load(data1)
            file2 = json.load(data2)

    return stylish(diff(file1, file2))
