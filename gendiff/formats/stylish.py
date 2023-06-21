from itertools import chain


FIRST_CHAR_KEY = 0
NUMBER_OF_INDENTS = 4
STARTING_DEPTH_VALUE = 0
THIRD_KEY_CHAR = 2


def get_correct_view(data_tree):
    replacement_values = (('True', 'true'),
                          ('False', 'false'),
                          ('None', 'null'))
    for values in replacement_values:
        data_tree = data_tree.replace(*values)
    return data_tree


def get_formated_dict(data):
    result = {}
    for key, value in data.items():
        if value['diff'] == 'nested':
            result['  ' + key] = get_formated_dict(value['children'])
        elif value['diff'] == 'added':
            result['+ ' + key] = value['value']
        elif value['diff'] == 'deleted':
            result['- ' + key] = value['value']
        elif value['diff'] == 'changed':
            result['- ' + key] = value['value1']
            result['+ ' + key] = value['value2']
        else:
            result['  ' + key] = value['value']

    return result


def get_stylish(data):
    formated_data = get_formated_dict(data)
    replacer = ' '
    spaces_count = NUMBER_OF_INDENTS

    def iter_(current_data, depth=STARTING_DEPTH_VALUE):
        if not isinstance(current_data, dict):
            return str(current_data)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_data.items():
            if key[FIRST_CHAR_KEY] in (' ', '+', '-'):
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}{key}: '
                             f'{iter_(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: '
                             f'{iter_(val, deep_indent_size)}')
        result = chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return get_correct_view(iter_(formated_data))
