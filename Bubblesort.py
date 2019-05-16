import numpy as np
from prettytable import PrettyTable
import sys



def create_sequence_array(bound, num_suquences):
    """
    Creates a 50x10000 array of sequences
    :param bound: int
    :return: array of 10000 sequences
    """

    sequence_array = []

    for i in range(num_suquences):
        sequence_array.append([np.random.randint(0, bound) for x in range(50)])

    return sequence_array


def find_calculated_average(bound, sequence_array, x):
    """
    :param bound: the bound
    :param sequence_array: array of sequences
    :param x: a number between 0 and bound
    :return: calculated average
    """

    hits = 0

    for sequence in sequence_array:

        if x in sequence:
            hits += 1


    q = hits/10000

    return 50 + (q - (q*50))/2


def find_real_average(bound, sequence_array, x):
    """
    :param bound: the bound
    :param sequence_array: array of 10000 sequences
    :param x: a random number between 0 and bound
    """
    steps = 0

    for sequence in sequence_array:

        if x in sequence:
            steps += sequence.index(x) + 1
        else:
            steps += 50

    return steps / 10000


if __name__ == "__main__":
    num_sequences = 10000
    bound_array = (30, 50, 80, 100, 1000, 10000, 100000, sys.maxsize)
    Table = PrettyTable(["Bound", "Calculated Average", "Real Average"])

    for bound in bound_array:
        x = np.random.randint(0, bound)
        sequence_array = create_sequence_array(bound, num_sequences)
        calculated_average = round(find_calculated_average(bound, sequence_array, x), 2)
        real_average = round(find_real_average(bound, sequence_array, x), 2)
        if bound == sys.maxsize:
            bound = "inf"
        Table.add_row([bound, calculated_average, real_average])

    print(Table)
