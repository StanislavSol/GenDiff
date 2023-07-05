def get_formatted_value(value):
    elem_types = {"<class 'NoneType'>": 'null',
                  "<class 'bool'>": str(value).lower(),
                  "<class 'str'>": f'\'{value}\'',
                  "<class 'int'>": value,
                  "<class 'dict'>": '[complex value]'}
    type_value = str(type(value))
    if type_value in elem_types:
        return elem_types[type_value]
    return value


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
