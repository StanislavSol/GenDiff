def get_formatted_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, bool):
        value = str(value).lower()
        return value
    elif isinstance(value, int):
        return value
    elif isinstance(value, str):
        return f'\'{value}\''
    elif value is None:
        return 'null'


def get_formatting_view(current_value, path=None, result=None):
    for key, value in current_value.items():
        path.append(key)
        if value['diff'] == 'nested':
            get_formatting_view(value['children'], path, result)
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
        path.pop()
    return result


def get_plain(data):
    result = get_formatting_view(data, path=[], result=[])
    return '\n'.join(result)
