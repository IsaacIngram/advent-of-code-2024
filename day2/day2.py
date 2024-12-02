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


def are_levels_safe(report) -> bool:
    previous = report[0]
    passed = True
    for level in report[1:]:
        if not (1 <= abs(level - previous) <= 3):
            return False
        previous = level
    return True


def main():

    with open(INPUT_PATH, 'r') as input_file:
        all_reports = [[int(i) for i in line.split()] for line in input_file.readlines()]

    part_1 = 0
    part_2 = 0
    for report in all_reports:
        if (sorted(report) == report or sorted(report, reverse=True) == report) and are_levels_safe(report):
                part_1 += 1
        else:
            for i in range(len(report)):
                new_report = report.copy()
                new_report.pop(i)
                if (sorted(new_report) == new_report or sorted(new_report, reverse=True) == new_report) and are_levels_safe(new_report):
                    part_2 += 1
                    break

    print(part_1)
    print(part_2 + part_1)

if __name__ == '__main__':
    main()

