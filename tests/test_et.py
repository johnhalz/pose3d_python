import pytest
import numpy as np

from sys import path
from pathlib import Path
path.append(Path(__file__).parents[1].as_posix())

from pose3d import ET

# Fixtures
@pytest.fixture
def et():
    return ET(dim=3)

# Tests
def test_ET_constructor():
    et1 = ET()
    et2 = ET(name="test", dim=2, vector=[1, 2])

    assert et1.name == ''
    assert et1.dim == 3
    assert np.all(et1.vector == np.zeros(3))

    assert et2.name == 'test'
    assert et2.dim == 2
    assert np.all(et2.vector == np.array([1, 2]))

    with pytest.raises(ValueError):
        et3 = ET(dim=4)
        et4 = ET(vector=[1, 2, 3, 4])

def test_ET_random(et):
    et.random()
    assert et.dim == 3
    assert et.vector.shape == (3,)
    assert np.all((et.vector >= 0) & (et.vector <= 1))

def test_ET_from_vector(et):
    et.from_vector([1, 2, 3])
    assert et.dim == 3
    assert np.all(et.vector == np.array([1, 2, 3]))

    with pytest.raises(ValueError):
        et.from_vector([1, 2, 3, 4])

def test_ET_zero(et):
    et.from_vector([1, 2, 3])
    et.zero()
    assert np.all(et.vector == np.zeros(3))

def test_ET_inv(et):
    et.from_vector([1, 2, 3])
    et.inv()
    assert np.all(et.vector == np.array([-1, -2, -3]))

def test_ET_getters(et):
    et.from_vector([1, 2, 3])
    assert et.dim == 3
    assert np.all(et.vector == np.array([1, 2, 3]))
    assert et.x == 1.0
    assert et.y == 2.0
    assert et.z == 3.0
    with pytest.raises(AttributeError):
        val = et.w
