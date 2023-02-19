import numpy as np


def fnc1():
    return np.random.randint(10)


def fnc2(x):
    return x * 2


def test_mock():
    data = fnc1()
    assert fnc2(data) <= 20
