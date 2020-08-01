# задание с одной звездочкой: написать декоратор в качестве объекта класса-секундомера

# import sys
# print (sys.path)

from validate_input import take_valid_input

import time

# from B5.B5_9 import validate_input as vi


class TimeThis:
    """
    class that acts as a function
    prints the average time of a single iteration based on user input
    returns the function
    """

    def __init__(self, num=10):
        self.num = num

    def __call__(self, func):
        return self.decorator(func)

    def decorator(self, func):
        def wrapper():
            avg_time = 0
            for _ in range(1, self.num + 1):
                t0 = time.time()
                func()
                t1 = time.time()
                print("iteration #{} -> {:.6f} seconds".format(_, t1 - t0))
                avg_time += (t1 - t0)
            print("\naverage time of a single iteration -> {:.6f} seconds".format(avg_time / self.num))

            return func()

        return wrapper


if __name__ == "__main__":

    # validating the user input for the number of iterations
    iter_number = take_valid_input()

    @TimeThis(iter_number)
    def f():
        for j in range(1000000):
            pass

    f()
