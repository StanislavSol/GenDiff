#!/usr/bin/env python3
import argparse
from ..parser import get_decoder_data
from ..diff import generate_diff
from ..formats.stylish import get_stylish
from ..formats.plain import get_plain


def get_reference():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compress two configuration' +
                                                 'files and shows a' +
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        default='stylish', help='set format of output')
    args = parser.parse_args()
    parsed_file = get_decoder_data(args.first_file, args.second_file)
    if args.format == 'plain':
        return generate_diff(*parsed_file, get_plain)
    return generate_diff(*parsed_file, get_stylish)


def main():
    print(get_reference())


if __name__ == '__main__':
    main()
