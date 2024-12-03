###############################################################################
#
# File: day3.py
#
# Author: Isaac Ingram
#
# Purpose:
#
###############################################################################
import re

MUL_PATTERN = r'mul\((\d{1,3}),(\d{1,3})\)'
INPUT_PATH = 'input.txt'

def main():

    with open(INPUT_PATH, 'r') as input_file:
        data = input_file.read()

    mul_regex = re.compile(MUL_PATTERN)

    part_1 = 0
    for match in mul_regex.finditer(data):
        part_1 += int(match.group(1)) * int(match.group(2))

    print(part_1)

if __name__ == '__main__':
    main()

