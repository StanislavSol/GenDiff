#!/usr/bin/env python3
from itertools import chain


FIRST_CHAR_KEY = 0
NUMBER_OF_INDENTS = 4
STARTING_DEPTH_VALUE = 0
THIRD_KEY_CHAR = 2


def get_formated_dict(value, replacer=' ', spaces_count=NUMBER_OF_INDENTS):
    def iter_(current_value, depth=STARTING_DEPTH_VALUE):
        if not isinstance(current_value, dict):
            return str(current_value)
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            if key[FIRST_CHAR_KEY] in (' ', '+', '-'):
                lines.append(f'{deep_indent[THIRD_KEY_CHAR:]}{key}: ' +
                             f'{iter_(val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}{key}: ' +
                             f'{iter_(val, deep_indent_size)}')
        result = chain('{', lines, [current_indent + '}'])
        result = map(lambda string: string.lower(), result)
        return '\n'.join(result)
    return iter_(value)
