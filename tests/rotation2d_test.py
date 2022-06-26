from sys import path
from os.path import dirname, join, abspath
path.insert(0, abspath(join(dirname(__file__), '..')))

from lib.rotation2d import Rotation2D

def euler2euler_test(angle: float, passing_cirteria: float = 0.001):

    rotation = Rotation2D()
    rotation.from_euler(angle, degree=True)

    assert (abs(angle - rotation.as_euler(degree=True))/angle) < passing_cirteria

    return True

def inv_test(angle: float, passing_cirteria: float = 0.001):

    rotation = Rotation2D()
    rotation.from_euler(angle, degree=True)
    rotation.inv()

    assert (abs(-angle - rotation.as_euler(degree=True))/angle) < passing_cirteria

    return True

def main():
    angle = 30

    test_passed = euler2euler_test(angle)
    if test_passed:
        print("euler2euler_test - Test Passed.")

    test_passed = inv_test(angle)
    if test_passed:
        print("inv_test - Test Passed.")

if __name__ == "__main__":
    main()