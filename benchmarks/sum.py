import pybm

from main import my_sum


def f():
    return my_sum(10000)


if __name__ == "__main__":
    pybm.run(module_context=globals())
