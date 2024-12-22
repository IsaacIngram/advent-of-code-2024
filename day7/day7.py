###############################################################################
#
# File: day7.py
#
# Author: Isaac Ingram
#
# Purpose:
#
###############################################################################
from itertools import product

INPUT_FILE = "input.txt"

def main():

    equations = list()

    with open(INPUT_FILE, 'r') as input_file:
        for line in input_file.readlines():
            # Get answer
            answer = int(line.split(":")[0])
            # Get values
            values = [int(value) for value in line.split(':')[1].split()]
            equations.append({"answer": answer, "values": values})

    part_1 = 0
    for equation in equations:
        answer = equation["answer"]
        values = equation["values"]

        for operation_permutation in list(product(['+', '*'], repeat=len(values) - 1)):
            sum_product = values[0]
            for i, operation in enumerate(operation_permutation):
                if operation == '+':
                    sum_product += values[i + 1]
                elif operation == '*':
                    sum_product *= values[i + 1]
            if sum_product == answer:
                part_1 += sum_product
                break
    print(part_1)






if __name__ == '__main__':
    main()
