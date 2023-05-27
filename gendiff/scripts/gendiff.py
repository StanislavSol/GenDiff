#!/usr/bin/env python3
import argparse


def get_help():
    parser = argparse.ArgumentParser(prog='gendiff',
                                     description='Compress two configuration' +
                                                 'files and shows a' +
                                                 'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', metavar='FORMAT', help='set format of output')
    args = parser.parse_args()
    return args


def main():
    get_help()


if __name__ == '__main__':
    main()
