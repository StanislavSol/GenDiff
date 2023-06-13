#!/usr/bin/env python3
from .formats.stylish import get_stylish
from .formats.plain import get_plain
from .formats.json import get_json
from .read_file import get_decoder_data
from .data_parsing import get_format_diff


def generate_diff(data1, data2, format_name):
    format_dictionary = {'stylish': get_stylish,
                         'plain': get_plain,
                         'json': get_json}
    reads_files = get_decoder_data(data1, data2)
    data_difference = get_format_diff(*reads_files)
    return format_dictionary[format_name](data_difference)
