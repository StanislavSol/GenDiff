LAST_ADDED_ELEM = -1


def get_formatted_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, int):
        return value
    elif isinstance(value, str):
        return f'\'{value}\''


def get_plain(data):
    def iter_(current_value, path=[], result=[]):
        for key, value in current_value.items():
            path.append(key)
            if value['diff'] == 'nested':
                iter_(value['children'], path)
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
        return '\n'.join(result)
    return iter_(data)
