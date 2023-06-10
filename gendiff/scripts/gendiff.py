#!/usr/bin/env python3
import argparse
from ..parser import get_decoder_data
from ..diff import gen_diff
from ..formats.stylish import get_stylish
from ..formats.plain import get_plain
from ..formats.json import get_json


def generate_diff():
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
    elif args.format == 'json':
        return generate_diff(*parsed_file, get_json)
    return generate_diff(*parsed_file, get_stylish)


def main():
    print(generate_diff())


if __name__ == '__main__':
    main()
