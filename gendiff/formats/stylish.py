from itertools import chain


FIRST_CHAR_KEY = 0
INDENT_WIDTH = 4
STARTING_DEPTH_VALUE = 0
THIRD_KEY_CHAR = 2
REPLACER = ' '
STATUSES = {'added': '+ ', 'deleted': '- ', 'unchanged': '  '}


def get_format_value(value):
    elem_types = {"<class 'NoneType'>": 'null',
                  "<class 'bool'>": str(value).lower()}
    type_value = str(type(value))
    if type_value in elem_types:
        return elem_types[type_value]
    return value


def get_format_view(current_data, depth=STARTING_DEPTH_VALUE):

    if not isinstance(current_data, dict):
        return str(current_data)

    indent_size = depth + INDENT_WIDTH
    deep_indent = REPLACER * indent_size
    current_indent = REPLACER * depth
    lines = []
    for key, val in current_data.items():
        if isinstance(val, dict) and 'diff' in val:

            if val['diff'] == 'nested':
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}  {key}: '
                             f'{get_format_view(val["children"], indent_size)}')

            elif val['diff'] == 'changed':

                needed_val = get_format_value(val['value1'])
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}- {key}: '
                             f'{get_format_view(needed_val, indent_size)}')

                needed_val = get_format_value(val['value2'])
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}+ {key}: '
                             f'{get_format_view(needed_val, indent_size)}')
            else:

                needed_val = get_format_value(val['value'])
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}'
                             f'{STATUSES[val["diff"]]}{key}: '
                             f'{get_format_view(needed_val, indent_size)}')
        else:
            needed_val = get_format_value(val)
            lines.append(f'{deep_indent}{key}: '
                         f'{get_format_view(needed_val, indent_size)}')

    result = chain('{', lines, [current_indent + '}'])
    return '\n'.join(result)


def get_stylish(data):
    result = get_format_view(data)
    return result
