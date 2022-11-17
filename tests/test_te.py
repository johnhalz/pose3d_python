import numpy as np

from pathlib import Path
from  sys import path
path.append(Path(__file__).parent.parent.as_posix())

from pose3d import TE


def test_te_init():
    te = TE(name='init_te', dim=2)
    assert te == np.zeros(2)

    if not te == np.zeros(2):
        print(te.vector())


def test_te_random():
    te = TE('random_te', dim=2)
    te.random()
    assert te == np.array([te.x(), te.y()])

    if not te == np.array([te.x(), te.y()]):
        print(te.vector())


def test_te_x():
    te = TE('x_te')
    te.random()
    assert (te.x() == te.vector()[0])

    if not te.x() == te.vector()[0]:
        print(te.x())
        print(te.vector()[0])


def test_te_y():
    te = TE('y_te')
    te.random()
    assert (te.y() == te.vector()[1])

    if not te.y() == te.vector()[1]:
        print(te.y())
        print(te.vector()[1])


def test_te_z():
    te = TE('y_te')
    te.random()
    assert (te.z() == te.vector()[2])

    if not te.y() == te.vector()[2]:
        print(te.y())
        print(te.vector()[2])

        
def test_te_zero():
    te_1 = TE('te_1')
    te_2 = TE('te_2')
    te_1.random()
    assert te_1 != te_2

    te_1.zero()

    assert te_1 == te_2


# def main():
#     test_te2_init()
#     test_te2_random()
#     test_te2_x()
#     test_te2_y()
#     test_te2_zero()

# if __name__ == '__main__':
#     main()