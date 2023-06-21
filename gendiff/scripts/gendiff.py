#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


def get_pars_args():
    parser = argparse.ArgumentParser(description='''
    Compress two configuration files and shows a difference.''')

    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT',
                        default='stylish', help='set format of output',
                        choices=['stylish', 'plain', 'json'])

    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


def main():
    print(generate_diff(*get_pars_args()))


if __name__ == '__main__':
    main()
