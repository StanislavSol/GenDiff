import json


def get_diff(file1, file2):
    result = []
    for key, value in file1.items():
        if key in file2:
            if file2[key] == value:
                result.append('   ' + key + ': ' + str(value) + '\n')
            else:
                result.append(' - ' + key + ': ' + str(value) + '\n')
                result.append(' + ' + key + ': ' + str(file2[key]) + '\n')
            del file2[key]
        else:
            result.append(' - ' + key + ': ' + str(value) + '\n')

    for key, value in file2.items():
        result.append(' + ' + key + ': ' + str(value) + '\n')

    result.sort(key=lambda key: key[3])
    return '{\n' + ''.join(result) + '}'


def generate_diff(file_path1, file_path2):
    with open(file_path1) as data1, open(file_path2) as data2:
        file1 = json.load(data1)
        file2 = json.load(data2)

    return get_diff(file1, file2)
