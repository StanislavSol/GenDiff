def get_format_diff(data1, data2):
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        if key not in data1:
            result[key] = {'diff': 'added',
                           'value': data2[key]}
        elif key not in data2:
            result[key] = {'diff': 'deleted',
                           'value': data1[key]}
        elif data1[key] == data2[key]:
            result[key] = {'diff': 'unchanged',
                           'value': data1[key]}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {'diff': 'nested',
                           'children': get_format_diff(data1[key], data2[key])}
        else:
            result[key] = {'diff': 'changed',
                           'value1': data1[key],
                           'value2': data2[key]}
        sorted_data = dict(sorted(result.items()))
    return sorted_data
