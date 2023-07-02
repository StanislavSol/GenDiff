from itertools import chain


FIRST_CHAR_KEY = 0
INDENT_WIDTH = 4
STARTING_DEPTH_VALUE = 0
THIRD_KEY_CHAR = 2
REPLACER = ' '
STATUSES = {'added': '+ ', 'deleted': '- ', 'unchanged': '  '}


def get_correct_view(data_tree):
    replacement_values = (('True', 'true'),
                          ('False', 'false'),
                          ('None', 'null'))
    for values in replacement_values:
        data_tree = data_tree.replace(*values)
    return data_tree


def get_stylish(current_data, depth=STARTING_DEPTH_VALUE):
    if not isinstance(current_data, dict):
        return str(current_data)

    indent_size = depth + INDENT_WIDTH
    deep_indent = REPLACER * indent_size
    current_indent = REPLACER * depth
    lines = []

    for key, value in current_data.items():
        if isinstance(value, dict) and 'diff' in value:

            if value['diff'] == 'nested':
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}  {key}: '
                             f'{get_stylish(value["children"], indent_size)}')

            elif value['diff'] == 'changed':
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}- {key}: '
                             f'{get_stylish(value["value1"], indent_size)}')

                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}+ {key}: '
                             f'{get_stylish(value["value2"], indent_size)}')
            else:
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}'
                             f'{STATUSES[value["diff"]]}{key}: '
                             f'{get_stylish(value["value"], indent_size)}')
        else:
            lines.append(f'{deep_indent}{key}: '
                         f'{get_stylish(value, indent_size)}')

    result = chain('{', lines, [current_indent + '}'])
    return get_correct_view('\n'.join(result))
