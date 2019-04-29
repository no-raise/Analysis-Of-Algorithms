import time
from prettytable import PrettyTable


def fib_recursive(x):
    if x <= 2:
        return 1
    return fib_recursive(x - 1) + fib_recursive(x - 2)


def fib_recursive_cached(x, cache=None):
    if cache is None:
        cache = {}
    if x in cache.keys():
        return cache[x]
    if x <= 2:
        return 1

    cache[x] = fib_recursive_cached(x - 1, cache) + fib_recursive_cached(x - 2, cache)

    return cache[x]


def fib_iterative(x):
    num1 = 1
    num2 = 1
    for i in range(2, x):
        temp = num2
        num2 = num1+num2
        num1 = temp
    return num2


if __name__ == "__main__":
    Table = PrettyTable(["n", "Fib_Iterative", "Fib_Recursive_Cached", "Fib(n)"])

    for i in range(0, 1000, 5):
        # start_time = time.time()
        # fib_recursive(i)
        # end_time = time.time()
        # time_fib = end_time - start_time

        start_time = time.time()
        fib_i = fib_iterative(i)
        end_time = time.time()
        time_itr = end_time - start_time

        start_time = time.time()
        fib_recursive_cached(i)
        end_time = time.time()
        time_recursive_cached = end_time - start_time

        Table.add_row([i, round(time_itr), round(time_recursive_cached), fib_i])

    print(Table)


