#!/usr/bin/env python3
import argparse
from ..diff import get_decoder_data
from ..stylish import get_formated_dict


def get_reference():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compress two configuration' +
                                                 'files and shows a' +
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        default=get_formated_dict, help='set format of output')
    args = parser.parse_args()
    finish_diff = get_decoder_data(args.first_file, args.second_file)
    print(args.format(finish_diff))


def main():
    get_reference()


if __name__ == '__main__':
    main()
