from gendiff.file_comparison import generate_diff


def get_files_with_recursion_yaml():
    path_file1 = 'tests/fixtures/recursive_data_yml/file1.yaml'
    path_file2 = 'tests/fixtures/recursive_data_yml/file2.yaml'
    path_sample_file = 'tests/fixtures/recursive_data_yml/sample_output_recursion.yaml'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read()[:-1]


def get_files_with_recursion_json():
    path_file1 = 'tests/fixtures/recursive_data_json/file_recursive1.json'
    path_file2 = 'tests/fixtures/recursive_data_json/file_recursive2.json'
    path_sample_file = 'tests/fixtures/recursive_data_json/sample_output_recursion.json'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read()[:-1]


def get_files_json():
    path_file1 = 'tests/fixtures/flat_data_json/file1.json'
    path_file2 = 'tests/fixtures/flat_data_json/file2.json'
    path_sample_file = 'tests/fixtures/flat_data_json/sample_output.json'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read()[:-1]


def get_files_yaml():
    path_file1 = 'tests/fixtures/flat_data_yml/file1.yml'
    path_file2 = 'tests/fixtures/flat_data_yml/file2.yml'
    path_sample_file = 'tests/fixtures/flat_data_yml/sample_output.yml'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read()[:-1]


def test_generate_diff():
    file_yaml1, file_yaml2, result_file_yaml = get_files_yaml()
    file_json1, file_json2, result_file_json = get_files_json()
    file_rec_json1, file_rec_json2, result_file_rec_json = get_files_with_recursion_json()
    file_rec_yml1, file_rec_yml2, result_file_rec_yml = get_files_with_recursion_yaml()
    assert generate_diff(file_yaml1, file_yaml2) == result_file_yaml
    assert generate_diff(file_json1, file_json2) == result_file_json
    assert generate_diff(file_rec_json1, file_rec_json2) == result_file_rec_json
    assert generate_diff(file_rec_yml1, file_rec_yml2) == result_file_rec_yml


