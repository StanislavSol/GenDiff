from gendiff import generate_diff
LAST_ELEM = -1


def get_files_with_recursion_yaml():
    path_file1 = 'tests/fixtures/recursive_data_yml/file1.yaml'
    path_file2 = 'tests/fixtures/recursive_data_yml/file2.yaml'
    path_sample_file = 'tests/fixtures/recursive_data_yml/' \
                       'sample_output_recursion.yaml'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()


def get_files_with_recursion_json():
    path_file1 = 'tests/fixtures/recursive_data_json/file1.json'
    path_file2 = 'tests/fixtures/recursive_data_json/file2.json'
    path_sample_file = 'tests/fixtures/recursive_data_json/' \
                       'sample_output_recursion.json'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()


def get_files_json():
    path_file1 = 'tests/fixtures/flat_data_json/file1.json'
    path_file2 = 'tests/fixtures/flat_data_json/file2.json'
    path_sample_file = 'tests/fixtures/flat_data_json/sample_output.json'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()


def get_files_yaml():
    path_file1 = 'tests/fixtures/flat_data_yml/file1.yml'
    path_file2 = 'tests/fixtures/flat_data_yml/file2.yml'
    path_sample_file = 'tests/fixtures/flat_data_yml/sample_output.yml'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read().rstrip()


def test_json():
    result_data = generate_diff(
                                *get_files_with_recursion_json()[:LAST_ELEM],
                                'json')
    sample_file = open('tests/fixtures/check_json.json', 'r').read().rstrip()
    verification_file = sample_file
    assert result_data == verification_file


def test_stylish():
    files_for_test = (get_files_yaml(),
                      get_files_json(),
                      get_files_with_recursion_json(),
                      get_files_with_recursion_yaml())

    for files in files_for_test:
        result_data = generate_diff(*files[:LAST_ELEM], 'stylish')
        verification_file = files[LAST_ELEM]
        assert result_data == verification_file


def test_plain():
    result_data = generate_diff(*get_files_with_recursion_json()[:LAST_ELEM],
                                'plain')
    sample_file = open('tests/fixtures/sample_file.json', 'r').read().rstrip()
    verification_file = sample_file
    assert result_data == verification_file
