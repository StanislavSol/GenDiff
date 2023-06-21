from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
from gendiff.formats.json import get_json
from gendiff.read_file import get_decoder_data
from gendiff.data_parsing import get_format_diff


def generate_diff(data1, data2, format_name='stylish'):
    format_dictionary = {'stylish': get_stylish,
                         'plain': get_plain,
                         'json': get_json}
    file_data1 = get_decoder_data(data1)
    file_data2 = get_decoder_data(data2)
    data_difference = get_format_diff(file_data1,
                                      file_data2)
    convert_format = format_dictionary[format_name](data_difference)

    return convert_format
