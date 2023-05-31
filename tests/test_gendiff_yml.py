from gendiff.file_comparison import generate_diff

def get_files():
    path_file1 = 'tests/fixtures/file1.yml'
    path_file2 = 'tests/fixtures/file2.yml'
    path_sample_file = 'tests/fixtures/sample_output.yml'
    with open(path_sample_file, 'r', encoding='utf=8') as sample:
        return path_file1, path_file2, sample.read()


def test_generate_diff():
    file1, file2, result_file = get_files()
    assert generate_diff(file1, file2) == result_file
