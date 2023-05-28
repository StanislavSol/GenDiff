#!/usr/bin/env python3
import argparse
from generators.file_comparison import generate_diff


def get_reference():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compress two configuration' +
                                                 'files and shows a' +
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        help='set format of output')
    args = parser.parse_args()
    dictionary_representation = vars(args)

    print(generate_diff(dictionary_representation['first_file'],
                        dictionary_representation['second_file']))


def main():
    get_reference()


if __name__ == '__main__':
    main()
