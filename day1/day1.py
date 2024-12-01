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

    all_left.sort()
    all_right.sort()
    accumulated_sum = 0
    for i in range(len(all_left)):
        accumulated_sum += abs(all_left[i] - all_right[i])

    print(accumulated_sum)


if __name__ == '__main__':
    main()
