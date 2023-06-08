#!/usr/bin/env python3
def get_type_value(value):
    if isinstance(value, dict):
        return 'mkdir'
    else:
        return 'mkfile'


def get_value_adjust(value):
    if value is False:
        return 'false'
    elif value is True:
        return 'true'
    elif value is None:
        return 'null'
    else:
        return value


def generate_diff(data1, data2):
    result = {}
    keys = data1.keys() | data2.keys()
    for key in keys:
        if key not in data1:
            result[key] = {'type': get_type_value(data2[key]),
                           'diff': 'added',
                           'value': get_value_adjust(data2[key])}
        elif key not in data2:
            result[key] = {'type': get_type_value(data1[key]),
                           'diff': 'deleted',
                           'value': get_value_adjust(data2[key])}
        elif data1[key] == data2[key]:
            result[key] = {'type': get_type_value(data1[key]),
                           'diff': 'unchanged',
                           'value1': get_value_adjust(data1[key]),
                           'value2': get_value_adjust(data2[key])}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {'type': 'mkdir','diff': 'changed', 'children': generate_diff(value1, value2)}
        else:
            result[key] = {'type': get_type_value(data1[key]),
                           'diff': 'changed',
                           'value1': get_value_adjust(data1[key]),
                           'value2': get_value_adjust(data2[key])}
    return dict(sorted(result.items()))

