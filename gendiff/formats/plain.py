LAST_ADDED_ELEM = -1


def get_correct_view(data_tree):
    replacement_values = (('True', 'true'),
                          ('False', 'false'),
                          ('None', 'null'))
    for values in replacement_values:
        data_tree = data_tree.replace(*values)
    return data_tree


def get_formatted_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return value
    elif isinstance(value, str):
        return f'\'{value}\''


def get_plain(current_value, path=[], result=[]):
    for key, value in current_value.items():
        path.append(key)
        if value['diff'] == 'nested':
            get_plain(value['children'], path)
            path = path[:LAST_ADDED_ELEM]
        elif value['diff'] == 'deleted':
            result.append(f'Property \'{".".join(path)}\' was removed')
        elif value['diff'] == 'added':
            result.append(f'Property \'{".".join(path)}\' was added '
                          f'with value: '
                          f'{get_formatted_value(value["value"])}')
        elif value['diff'] == 'changed':
            result.append(f'Property \'{".".join(path)}\''
                          f' was updated. From '
                          f'{get_formatted_value(value["value1"])} to '
                          f'{get_formatted_value(value["value2"])}')
        path = path[:LAST_ADDED_ELEM]
    return get_correct_view('\n'.join(result))
