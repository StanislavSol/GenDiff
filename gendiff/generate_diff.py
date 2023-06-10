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


def get_format_diff(data1, data2):
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
                           'value': get_value_adjust(data1[key])}
        elif data1[key] == data2[key]:
            result[key] = {'type': get_type_value(data1[key]),
                           'diff': 'unchanged',
                           'value': get_value_adjust(data1[key])}
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            result[key] = {'type': 'mkdir',
                           'diff': 'changed',
                           'children': get_format_diff(data1[key], data2[key])}
        else:
            result[key] = {'type': 'mkfile',
                           'diff': 'changed',
                           'value1': get_value_adjust(data1[key]),
                           'value2': get_value_adjust(data2[key])}
        sorted_data = dict(sorted(result.items()))
    return sorted_data


def generate_diff(data1, data2, format_name):
    return format_name(get_format_diff(data1, data2))
