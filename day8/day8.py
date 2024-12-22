
INPUT_FILE = 'input.txt'

def main():

    frequency_map = dict() # Map of frequency name to all points
    point_list = list() # 2D list of frequencies at each point


    with open(INPUT_FILE, 'r') as input_file:
        for y, line in enumerate(input_file.readlines()):
            point_list.append(list())
            line = line.strip()
            for x, frequency in enumerate(line):
                if frequency != '.':
                    if frequency not in frequency_map:
                        frequency_map[frequency] = list()
                    frequency_map[frequency].append((x, y))
                point_list[y].append(frequency)

    part_1 = 0
    # Iterate through all possible frequencies
    for frequency in frequency_map:
        # Iterate through all points where this frequency appears
        for root_x, root_y in frequency_map[frequency]:
            # Iterate through all OTHER points where this frequency appears
            for other_x, other_y in frequency_map[frequency]:
                if root_x == other_x and root_y == other_y:
                    # Skip if point is the same
                    continue

                delta_x = other_x - root_x
                delta_y = other_y - root_y
                new_y = root_y - delta_y
                new_x = root_x - delta_x
                if 0 <= new_y < len(point_list) and 0 <= new_x < len(point_list[0]):
                    if point_list[new_y][new_x] != '#':
                        point_list[new_y][new_x] = '#'
                        part_1 += 1

    print(part_1)

if __name__ == '__main__':
    main()

