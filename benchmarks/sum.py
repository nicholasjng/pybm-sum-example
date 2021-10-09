import os
import sys

import pybm

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from main import my_sum


def f():
    return my_sum(100000)


if __name__ == "__main__":
    pybm.run(context=globals())
