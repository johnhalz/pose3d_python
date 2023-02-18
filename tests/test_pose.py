import numpy as np
import pytest

from sys import path
from pathlib import Path
path.append(Path(__file__).parents[1].as_posix())

from pose3d import Pose

@pytest.fixture
def pose():
    return Pose(name='Test', et_dim=3, er_dim=3)

def test_pose_init(pose):
    assert pose.name == 'Test'
    assert pose.position.dim == 3
    assert pose.orientation.dim == 3

def test_pose_random(pose):
    pose.random()
    assert np.all(pose.position.vector != np.zeros(3))
    assert np.all(pose.orientation.as_quat() != np.array([1., 0., 0., 0.]))

def test_pose_zero(pose):
    pose.zero()
    assert np.all(pose.position.vector == np.zeros(3))
    assert np.all(pose.orientation.as_quat() == np.array([0., 0., 0., 1.]))

def test_pose_dims(pose):
    assert pose.dims() == (3, 3)
