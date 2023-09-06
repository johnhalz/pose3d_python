from pose3d import Pose

import numpy as np
import pytest


@pytest.fixture
def pose():
    return Pose(name='Test')


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
