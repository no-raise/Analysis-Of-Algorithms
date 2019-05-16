from prettytable import PrettyTable
import numpy as np



def create_sequence_array(bound,n,num_sequences):
    """
    Creates a 50x10000 array of sequences
    :param bound: int
    :return: array of 10000 sequences
    """

    sequence_array = []

    for i in range(num_sequences):
        sequence_array.append([np.random.randint(0, bound) for x in range(n)])

    return sequence_array


def insertion_mod(sequence_array):
    steps = 0
    for sequence in sequence_array:
        for i, num in enumerate(sequence):
            j = i
            while j != 0 and sequence[j] < sequence[j-1]:
                temp = sequence[j]
                sequence[j] = sequence[j-1]
                sequence[j-1] = temp
                steps += 1
                j -= 1

    return steps/10


if __name__ == "__main__":
    num_sequences = 10
    bound = 10000
    n_range = [100, 500, 1000, 2500, 3000, 3500]
    Table = PrettyTable(["Input Size", "Calculated Average", "Real Average"])
    for n in n_range:
        sequence_array = create_sequence_array(bound, n, num_sequences)
        calculated_average = (n*n)/4 + (3*n)/4
        real_average = round(insertion_mod(sequence_array), 2)
        Table.add_row([n, calculated_average, real_average])

    print(Table)

