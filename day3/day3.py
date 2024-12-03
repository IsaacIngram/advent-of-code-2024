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
DO_PATTERN = r'do\(\)'
DONT_PATTERN = r"don't\(\)"
INPUT_PATH = 'input.txt'

def main():

    with open(INPUT_PATH, 'r') as input_file:
        data = input_file.read()
    mul_regex = re.compile(MUL_PATTERN)

    part_1 = 0
    for match in mul_regex.finditer(data):
        part_1 += int(match.group(1)) * int(match.group(2))
    print(part_1)

    part_2 = 0
    split_data = re.split(DO_PATTERN, data)
    for after_do in split_data:
        before_dont = re.split(DONT_PATTERN, after_do)[0]
        for match in mul_regex.finditer(before_dont):
            part_2 += int(match.group(1)) * int(match.group(2))
    print(part_2)

if __name__ == '__main__':
    main()

