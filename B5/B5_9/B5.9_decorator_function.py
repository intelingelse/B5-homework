import time

from validate_input import take_valid_input


def time_this(num=10):  # external function that accepts the number of iterations to be executed
    def decorator(func):  # decorator function that accepts a function to be run
        def wrapper():  # function that wraps the function to be run
            timing = 0
            for _ in range(1, num + 1):
                iter_time = 0
                t0 = time.time()
                func()
                t1 = time.time()
                iter_time = t1 - t0
                print("iteration #{} -> {:.6f} seconds".format(_, iter_time))
                timing += (t1 - t0)
            print("\naverage time of a single iteration -> {:.6f} seconds".format(timing / num))
            return func()  # wrapper function returns function that was executed

        return wrapper  # decorator function returns wrapper function

    return decorator  # time_this function returns decorator function


if __name__ == "__main__":

    # validating the user input for the number of iterations
    iter_number = take_valid_input()


    @time_this(iter_number)
    def f():
        for j in range(1000000):
            pass


    f()
