###############################################################################
#
# File: day5.py
#
# Author: Isaac Ingram
#
# Purpose:
#
###############################################################################

INPUT_PATH = 'input.txt'

def main():

    adjacency_list = dict()
    read_updates = False
    updates_to_perform = list()
    with open(INPUT_PATH, 'r') as input_file:
        for line in input_file.readlines():
            # Switch to reading updates when empty line is encountered
            if line == "\n":
                read_updates = True
                continue
            if not read_updates:
                # Reading in adjacency list
                before_s, after_s = line.split("|")
                if int(before_s) in adjacency_list:
                    adjacency_list[int(before_s)].add(int(after_s))
                else:
                    adjacency_list[int(before_s)] = set()
                    adjacency_list[int(before_s)].add(int(after_s))
            else:
                # Reading in updates
                updates_to_perform.append([int(x) for x in line.split(",")])

    part1 = 0
    part2 = 0
    for page_update in updates_to_perform:
        is_ordered = True
        for i in range(len(page_update)):
            for j in range(i + 1, len(page_update)):
                if page_update[j] not in adjacency_list[page_update[i]]:
                    is_ordered = False
        if is_ordered:
            part1 += page_update[len(page_update) // 2]
        else:
            # Need to reorder
            for i in range(len(page_update) - 1, 0, -1):
                for j in range(i - 1, -1, -1):
                    current_val = page_update[i]
                    compared_val = page_update[j]
                    if compared_val in adjacency_list[current_val]:
                        # Swap
                        page_update[i], page_update[j] = page_update[j], page_update[i]
            part2 += page_update[len(page_update) // 2]

    print(part1)
    print(part2)

if __name__ == '__main__':
    main()
