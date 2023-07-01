from gendiff.formats.stylish import get_stylish
from gendiff.formats.plain import get_plain
from gendiff.formats.json import get_json
from gendiff.read_file import get_decoder_data
from gendiff.data_parsing import get_format_diff


def generate_diff(first_file, second_file, format_name='stylish'):
    formats = {'stylish': get_stylish,
               'plain': get_plain,
               'json': get_json}
    file_data1 = get_decoder_data(first_file)
    file_data2 = get_decoder_data(second_file)
    data_difference = get_format_diff(file_data1,
                                      file_data2)
    convert_format = formats[format_name](data_difference)

    return convert_format
