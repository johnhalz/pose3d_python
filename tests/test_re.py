import numpy as np

from pathlib import Path
from  sys import path
path.append(Path(__file__).parent.parent.as_posix())

from pose3d import ER

RE_TOLERANCE = 1e-10

def test_re_init():
    re = ER(name='init_re')
    assert np.array_equal(re.as_matrix(), np.eye(3))

def test_re_random():
    re = ER(name='random_re')
    re.random()
    assert not np.array_equal(re.as_quat(), [0, 0, 0, 1])

def test_re_quat():
    re = ER(name='re1')

    re.random()
    quaternion_1 = re.as_quat()
    re.random()
    re.from_quat(quaternion_1)

    assert np.allclose(re.as_quat(),
                       quaternion_1,
                       rtol=RE_TOLERANCE,
                       atol=RE_TOLERANCE)

def test_re_matrix():
    re = ER(name='re1')

    re.random()
    matrix_1 = re.as_matrix()
    re.random()
    re.from_matrix(matrix_1)

    assert np.allclose(re.as_matrix(),
                       matrix_1,
                       rtol=RE_TOLERANCE,
                       atol=RE_TOLERANCE)

def test_re_angle_axis():
    re = ER(name='re1')

    re.random()
    angle_axis_1 = re.as_angle_axis()
    re.random()
    re.from_angle_axis(angle_axis_1)

    assert np.allclose(re.as_angle_axis(),
                       angle_axis_1,
                       rtol=RE_TOLERANCE,
                       atol=RE_TOLERANCE)

def test_re_euler():
    re = ER(name='re1')

    # Test for units in degrees and radians
    for degree_opt in [True, False]:
        sequence = 'xyz'

        re.random()
        euler_1 = re.as_euler(sequence, degree_opt)
        re.random()
        re.from_euler(sequence, euler_1, degree_opt)

        assert np.allclose(re.as_euler(sequence, degree_opt),
                           euler_1,
                           rtol=RE_TOLERANCE,
                           atol=RE_TOLERANCE)

def test_re_apply_and_inv():
    re = ER(name='re1')

    random_vector = np.random.rand(3)

    rotated_vector = re.apply(random_vector)
    re.inv()
    rotated_vector = re.apply(rotated_vector)
    assert np.array_equal(random_vector, rotated_vector)

def test_re_eq():
    re1 = ER(name='re1')
    re2 = ER(name='re2')

    re1.random()
    re2.from_quat(re1.as_quat())

    assert re1 == re2

    re2.random()

    assert re1 != re2