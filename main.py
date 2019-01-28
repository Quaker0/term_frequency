#!/usr/bin/env python
import re
from collections import defaultdict


class WordCount():
    counter = {}

    def __init__(word):
        pass


def main():
    super_dict = {}
    print('ok')
    with open('pride-and-prejudice.txt', 'r') as text_file:
        for line in text_file.readlines():
            for word in line.split():
                word = formatter(word)
                if word not in super_dict:
                    super_dict[word] = 0

                super_dict[word] += 1


    print(super_dict)


def formatter(word):
    replace_with = '.,-?!:;()"'
    return re.sub(replace_with, '', word)


main()
