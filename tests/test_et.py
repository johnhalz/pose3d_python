from pose3d import ET

import pytest
import numpy as np


# Fixtures
@pytest.fixture
def et():
    return ET(dim=3)


# Tests
def test_et_constructor():
    et1 = ET()
    et2 = ET(name="test", vector=[1, 2])

    assert et1.name == ''
    assert et1.dim == 3
    assert np.all(et1.vector == np.zeros(3))

    assert et2.name == 'test'
    assert et2.dim == 2
    assert np.all(et2.vector == np.array([1, 2]))


def test_et_random(et):
    et.random()
    assert et.dim == 3
    assert et.vector.shape == (3,)


def test_et_vector_setter(et):
    et.vector = [1, 2, 3]
    assert et.dim == 3
    assert np.all(et.vector == np.array([1, 2, 3]))

    with pytest.raises(ValueError):
        et.vector = [1, 2, 3, 4]


def test_et_zero(et):
    et.vector = [1, 2, 3]
    et.zero()
    assert np.all(et.vector == np.zeros(3))


def test_et_inv(et):
    et.vector = [1, 2, 3]
    et.inv()
    assert np.all(et.vector == np.array([-1, -2, -3]))


def test_et_getters(et):
    et.vector = [1, 2, 3]
    assert et.dim == 3
    assert np.all(et.vector == np.array([1, 2, 3]))
    assert et.x == 1.0
    assert et.y == 2.0
    assert et.z == 3.0
