#!/usr/bin/env python3
import argparse
from ..parser import get_decoder_data
from ..diff import generate_diff
from ..formats.stylish import get_stylish


def get_reference():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compress two configuration' +
                                                 'files and shows a' +
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        default=get_stylish, help='set format of output')
    args = parser.parse_args()
    parsed_file = get_decoder_data(args.first_file, args.second_file)
    finish_diff = generate_diff(*parsed_file)
    print(args.format(finish_diff))


def main():
    get_reference()


if __name__ == '__main__':
    main()
