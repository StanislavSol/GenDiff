from itertools import chain


FIRST_CHAR_KEY = 0
INDENT_WIDTH = 4
STARTING_DEPTH_VALUE = 0
THIRD_KEY_CHAR = 2


def get_correct_view(data_tree):
    replacement_values = (('True', 'true'),
                          ('False', 'false'),
                          ('None', 'null'))
    for values in replacement_values:
        data_tree = data_tree.replace(*values)
    return data_tree


def get_stylish(data):
    replacer = ' '
    spaces_count = INDENT_WIDTH

    def iter_(current_data, depth=STARTING_DEPTH_VALUE):
        if not isinstance(current_data, dict):
            return str(current_data)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, value in current_data.items():
            if isinstance(value, dict) and 'diff' in value:

                if value['diff'] == 'nested':
                    lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}  {key}: '
                                 f'{iter_(value["children"], deep_indent_size)}')

                elif value['diff'] == 'added':
                    lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}+ {key}: '
                                 f'{iter_(value["value"], deep_indent_size)}')

                elif value['diff'] == 'deleted':
                    lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}- {key}: '
                                 f'{iter_(value["value"], deep_indent_size)}')

                elif value['diff'] == 'changed':
                    lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}- {key}: '
                                 f'{iter_(value["value1"], deep_indent_size)}')
                    lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}+ {key}: '
                                 f'{iter_(value["value2"], deep_indent_size)}')

                elif value['diff'] == 'unchanged':
                    lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}  {key}: '
                                 f'{iter_(value["value"], deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: '
                             f'{iter_(value, deep_indent_size)}')

        result = chain('{', lines, [current_indent + '}'])
        return '\n'.join(result)
    return get_correct_view(iter_(data))
