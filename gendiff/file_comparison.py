import json
import yaml


def get_diff(file1, file2):
    result = []
    for key, value in file1.items():
        if key in file2:
            if file2[key] == value:
                result.append('    ' + key + ': ' + str(value) + '\n')
            else:
                result.append('  - ' + key + ': ' + str(value) + '\n')
                result.append('  + ' + key + ': ' + str(file2[key]) + '\n')
            del file2[key]
        else:
            result.append('  - ' + key + ': ' + str(value) + '\n')

    for key, value in file2.items():
        result.append('  + ' + key + ': ' + str(value) + '\n')
    result = map(lambda string: string.lower(),
                 sorted(result, key=lambda key: key[4]))
    return '{\n' + ''.join(result) + '}\n'


def generate_diff(file_path1, file_path2):
    if 'yml' in file_path1 or 'yaml' in file_path1:
        with open(file_path1) as data1, open(file_path2) as data2:
            file1 = yaml.safe_load(data1)
            file2 = yaml.safe_load(data2)
    else:
        with open(file_path1) as data1, open(file_path2) as data2:
            file1 = json.load(data1)
            file2 = json.load(data2)

    return get_diff(file1, file2)
