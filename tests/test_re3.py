import numpy as np

from pathlib import Path
from  sys import path
path.append(Path(__file__).parent.parent.as_posix())

print(path)

from pose3d import RE3

def test_re3_init():
    re = RE3(name='init_re')
    re.random()
    re.identity()
    assert np.array_equal(re.as_matrix(), np.eye(3))

def test_re3_random():
    re = RE3(name='random_re')
    assert not np.array_equal(re.as_quat(), np.zeros(4))

def test_re3_quat():
    re = RE3(name='re1')

    re.random()
    quaternion_1 = re.as_quat()
    re.random()
    re.from_quat(quaternion_1)

    assert np.array_equal(re.as_quat(), quaternion_1)

def test_re3_matrix():
    re = RE3(name='re1')

    re.random()
    matrix_1 = re.as_matrix()
    re.random()
    re.from_matrix(matrix_1)

    assert np.array_equal(re.as_matrix(), matrix_1)

def test_re3_angle_axis():
    re = RE3(name='re1')

    re.random()
    angle_axis_1 = re.as_angle_axis()
    re.random()
    re.from_angle_axis(angle_axis_1)

    assert np.array_equal(re.as_angle_axis(), angle_axis_1)

def test_re3_euler():
    re = RE3(name='re1')

    # Test for units in degrees and radians
    for degree_opt in [True, False]:
        sequence = 'xyz'

        re.random()
        euler_1 = re.as_euler(sequence, degree_opt)
        re.random()
        re.from_euler(sequence, euler_1, degree_opt)

        assert np.array_equal(re.as_euler(sequence, degree_opt), euler_1)

def test_re3_inv():
    re = RE3(name='re1')

    re.random()
    quaternion = re.as_quat()

    re.inv()
    re.inv()
    assert np.array_equal(quaternion, re.as_quat())

def test_re3_apply():
    re = RE3(name='re1')

    random_vector = np.random.rand(3)

    rotated_vector = re.apply(random_vector)
    re.inv()
    rotated_vector = re.apply(rotated_vector)
    assert np.array_equal(random_vector, rotated_vector)

def test_re3_eq():
    re1 = RE3(name='re1')
    re2 = RE3(name='re2')

    re1.random()
    print(re1)
    print(re1.as_quat())
    re2.from_quat(re1.as_quat())

    assert re1 == re2

    re2.random()

    assert re1 != re2

