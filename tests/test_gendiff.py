from gendiff.generators.file_comparison import generate_diff
import json

def get_files():
    path_file1 = '/home/ssol/python-project-50/tests/fixtures/file1.json'
    path_file2 = '/home/ssol/python-project-50/tests/fixtures/file2.json'
    path_sample_file = '/home/ssol/python-project-50/tests/fixtures/sample_output.json'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read()


def test_generate_diff():
    file1, file2, result_file = get_files()
    assert generate_diff(file1, file2) == result_file
