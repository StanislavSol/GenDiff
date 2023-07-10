from gendiff import generate_diff
import pytest


@pytest.mark.parametrize('path1, path2, formatter, expected', [
    ('tests/fixtures/flat_file1.json',
     'tests/fixtures/flat_file2.json', 'stylish',
     'tests/fixtures/result_flat_file.txt'),
    ('tests/fixtures/recursion_file1.json',
     'tests/fixtures/recursion_file2.yaml', 'stylish',
     'tests/fixtures/recursion_result.txt'),
    ('tests/fixtures/recursion_file1.json',
     'tests/fixtures/recursion_file2.yaml', 'plain',
     'tests/fixtures/plain_result.txt'),
    ('tests/fixtures/recursion_file1.json',
     'tests/fixtures/recursion_file2.yaml', 'json',
     'tests/fixtures/result_json_format.txt')])
def test_generat_diff(path1, path2, formatter, expected):
    with open(expected, 'r') as file:
        res = file.read().strip()
    assert generate_diff(path1, path2, formatter) == res
