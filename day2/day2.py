###############################################################################
#
# File: day2.py
#
# Author: Isaac Ingram
#
# Purpose:
#
###############################################################################

INPUT_PATH = "input.txt"

def main():

    all_reports = list()
    with open(INPUT_PATH, 'r') as input_file:
        for line in input_file.readlines():
            split_line = line.split()
            report = list()
            for i in split_line:
                report.append(int(i))
            all_reports.append(report)

    part_1 = 0
    for report in all_reports:
        if sorted(report) == report or sorted(report, reverse=True) == report:
            previous = report[0]
            passed = True
            for level in report[1:]:
                if not (1 <= abs(level - previous) <= 3):
                    passed = False
                previous = level
            if passed:
                part_1 += 1

    print(part_1)

if __name__ == '__main__':
    main()

