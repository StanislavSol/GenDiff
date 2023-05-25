#!/usr/bin/env python3
import argparse


def get_help():
    parser = argparse.ArgumentParser(prog='gendiff', description=f'Compress two configuration'
                                                 f'files and shows a' 
                                                 f'difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    return args


def main():
    get_help()


if __name__ == '__main__':
    main()
