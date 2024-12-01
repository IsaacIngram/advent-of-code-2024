###############################################################################
#
# File: day1.py
#
# Author: Isaac Ingram
#
# Purpose:
#
###############################################################################

INPUT_PATH = "input.txt"

def main():

    all_left = list()
    all_right = list()

    with open(INPUT_PATH, 'r') as input_file:
        for line in input_file.readlines():
            split_line = line.split()
            all_left.append(int(split_line[0].strip()))
            all_right.append(int(split_line[1].strip()))

    accumulated_sum = 0
    for left_number in all_left:
        occurrences = all_right.count(left_number)
        accumulated_sum += left_number * occurrences

    print(accumulated_sum)


if __name__ == '__main__':
    main()
