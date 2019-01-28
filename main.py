#!/usr/bin/env python3
import re
import sys
from collections import defaultdict


def main(file_name):
    super_dict = defaultdict(int)
    stop_words = {word for word in read_file('stop_words.txt').split(',')}

    for word in re.split('[^a-zA-Z]', read_file(f'{file_name}.txt')):
        if len(word) > 1 and word not in stop_words:
            super_dict[word.lower()] += 1

    for word, count in sorted(super_dict.items(), key=lambda args: args[::-1]):
        print(word, '-', count)


def read_file(file_name):
    with open(file_name, 'r') as text_file:
        return text_file.read()


main(*sys.argv[1:])
