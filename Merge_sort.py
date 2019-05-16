from prettytable import PrettyTable
import numpy as np
import time


def create_array(n, bound):
    """
    Creates a random array
    :param bound: int
    :param n: int
    :return: random array
    """
    array = [np.random.randint(0, bound) for x in range(n)]
    return array


def insertion_sort(array):
    for i, num in enumerate(array):
        j = i
        while j != 0 and array[j] < array[j-1]:
            temp = array[j]
            array[j] = array[j-1]
            array[j-1] = temp
            j -= 1

    return array


def merge_sort(num_array):
    if len(num_array) < 2:
        return num_array[:len(num_array)]

    mid = len(num_array) // 2
    left = merge_sort(num_array[:mid])
    right = merge_sort(num_array[mid:])

    sorted_array = merge(left, right)

    return sorted_array


def merge(left, right):

    c = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            c.append(left[i])
            i += 1
        else:
            c.append(right[j])
            j += 1

    c.extend(left[i:])
    c.extend(right[j:])
    return c


if __name__=="__main__":
    bound = 100
    input_sizes = [100, 1000, 10000, 100000, 200000]
    Table = PrettyTable(["Input Size", "Insertion Sort", "Merge Sort"])
    for size in input_sizes:
        array = create_array(size, bound)
        array_copy = list(array)

        start_time = time.process_time()
        insertion_sort(array)
        end_time = time.process_time()
        time_insertion_sort = end_time - start_time

        start_time = time.process_time()
        merge_sort(array_copy)
        end_time = time.process_time()
        time_merge_sort = end_time - start_time

        Table.add_row([size, round(time_insertion_sort, 2), round(time_merge_sort, 2)])

    print(Table)

    print(time.time(), time.process_time())




