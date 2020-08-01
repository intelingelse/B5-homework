# задание с двумя звездочками: написать декоратор в качестве объекта класса-секундомера,
# который можно использовать как контекстный менеджер.

import time
# pycharm way
# from B5.B5_9 import validate_input as vi

# terminal way
from validate_input import take_valid_input

class TimeThis:
    """
    context manager class that measures the time it takes to execute a function
    prints average time based on the number of iterations given by a user
    """

    def __init__(self, num=10):  # default value of iterations is 10
        self.num = int(float(num))  # in case user passes float value, like 10.15 convert it to int

    def __enter__(self):
        return self

    def __exit__(self, *args, **kwargs):
        pass

    def __call__(self, func):  # __call__ method will add the function behavior
        print(f"measuring average time of a single execution of {func} based on {self.num} iterations")
        start = time.time()
        for _ in range(1, self.num + 1):
            func()
        end = time.time()
        total_time = end - start
        avg_time = total_time / self.num
        print("average time of a single iteration -> {:.6f} second(s)".format(avg_time))


if __name__ == '__main__':
    def f():
        for j in range(1000000):
            pass


    # validating the user input for the number of iterations
    iter_number = take_valid_input()

    with TimeThis(iter_number) as stopwatch:
        stopwatch(f)
