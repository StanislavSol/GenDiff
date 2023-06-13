#!/usr/bin/env python3
import argparse
from gendiff import generate_diff


parser = argparse.ArgumentParser(description='''
Compress two configuration files and shows a difference.''')

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument('-f', '--format', metavar='FORMAT',
                    default='stylish', help='set format of output')

args = parser.parse_args()


def main():
    print(generate_diff(args.first_file,
                        args.second_file,
                        args.format))


if __name__ == '__main__':
    main()
