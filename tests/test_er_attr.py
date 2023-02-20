import numpy as np
import pytest

from sys import path
from pathlib import Path
path.append(Path(__file__).parents[1].as_posix())

from pose3d import ERAttr

def test_er_default_constructor():
    r = ERAttr()
    assert r.name == ''
    assert r.dim == 3
    assert np.allclose(r.as_quat(), np.array([0, 0, 0, 1]), rtol=1e-6, atol=1e-6)

def test_er_constructor_with_args():
    r = ERAttr('test', dim=2)
    assert r.name == 'test'
    assert r.dim == 2
    assert np.allclose(r.as_quat(), np.array([0, 0, 0, 1]), rtol=1e-6, atol=1e-6)

def test_er_identity():
    r = ERAttr()
    r.random()
    r.identity()
    assert np.allclose(r.as_quat(), np.array([0, 0, 0, 1]), rtol=1e-6, atol=1e-6)

def test_er_inv():
    r = ERAttr()
    r.random()
    r_inv = r.as_matrix()
    r_inv = np.linalg.inv(r_inv)
    r.inv()
    assert np.allclose(r.as_matrix(), r_inv, rtol=1e-6, atol=1e-6)

def test_er_random():
    r1 = ERAttr()
    r1.random()
    r2 = ERAttr()
    r2.random()
    assert r1 != r2

def test_er_from_quat():
    r = ERAttr()
    r.from_quat(np.array([0.707107, 0, 0, 0.707107]))
    assert np.allclose(r.as_quat(), np.array([0.707107, 0, 0, 0.707107]), rtol=1e-6, atol=1e-6)

def test_er_from_matrix():
    # Test 3D rotation
    er = ERAttr(dim=3)
    er2 = ERAttr(dim=3)
    er2.random()
    er.from_matrix(er2.as_matrix())
    assert np.allclose(er2.as_matrix(), er.as_matrix())

    # Test 2D rotation
    er = ERAttr(dim=2)
    er2 = ERAttr(dim=2)
    er2.random()
    er.from_matrix(er2.as_matrix())
    assert np.allclose(er2.as_matrix(), er.as_matrix())

def test_er_from_angle_axis():
    # Test 3D rotation
    er = ERAttr(dim=3)
    er.random()
    er2 = ERAttr(dim=3)
    er2.from_angle_axis(er.as_angle_axis())
    assert np.allclose(er.as_angle_axis(), er2.as_angle_axis())

    # Test 2D rotation
    er = ERAttr(dim=2)
    with pytest.raises(AttributeError):
        er.from_angle_axis(np.random.uniform(-np.pi, np.pi, size=(2,)))

def test_er_from_euler():
    # Test 3D rotation
    er = ERAttr(dim=3)
    angles = np.random.uniform(-np.pi, np.pi, size=(3,))
    er.from_euler(sequence='xyz', angles=angles)
    assert np.allclose(er.as_euler(sequence='xyz'), angles)

    # Test 2D rotation
    er = ERAttr(dim=2)
    angles = np.random.uniform(-np.pi, np.pi)
    er.from_euler(sequence=None, angles=angles)
    assert np.allclose(er.as_euler(sequence=None), angles)

def test_er_dim():
    r = ERAttr(dim=2)
    assert r.dim == 2

def test_as_quat():
    er = ERAttr()
    quat = er.as_quat()
    assert isinstance(quat, np.ndarray)
    assert quat.shape == (4,)
    assert np.allclose(quat, np.array([0, 0, 0, 1]))

    # test with non-default values
    er = ERAttr(name='test', dim=2)
    er.random()
    quat = er.as_quat()
    assert isinstance(quat, np.ndarray)
    assert quat.shape == (4,)
    assert np.allclose(np.linalg.norm(quat), 1.0, rtol=1e-6)

def test_as_matrix():
    er = ERAttr()
    matrix = er.as_matrix()
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (3, 3)
    assert np.allclose(matrix, np.eye(3))

    # Test with non-default values
    er = ERAttr(name='test', dim=2)
    er.random()
    matrix = er.as_matrix()
    assert isinstance(matrix, np.ndarray)
    assert matrix.shape == (2, 2)
    assert np.allclose(np.dot(matrix, matrix.T), np.eye(2), rtol=1e-6)

def test_as_angle_axis():
    er = ERAttr()
    angle_axis = er.as_angle_axis()
    assert isinstance(angle_axis, np.ndarray)
    assert angle_axis.shape == (3,)
    assert np.allclose(angle_axis, np.array([0, 0, 0]))

    # Test with non-default values
    er = ERAttr(name='test', dim=3)
    er.random()
    angle_axis = er.as_angle_axis()
    assert isinstance(angle_axis, np.ndarray)
    assert angle_axis.shape == (3,)
    assert np.isclose(np.linalg.norm(angle_axis), 1.0, rtol=1e-6)

def test_as_euler():
    er = ERAttr()
    euler = er.as_euler('xyz')
    assert isinstance(euler, np.ndarray)
    assert np.allclose(euler, [0.0, 0.0, 0.0])

    # Test with non-default values
    er = ERAttr(name='test', dim=2)
    er.random()
    euler = er.as_euler(degrees=True)
    assert isinstance(euler, float)
    assert np.abs(euler) <= 360

def test_er_apply():
    # Test 3D rotation
    er = ERAttr(dim=3)
    er.random()
    vec = np.random.uniform(-10, 10, size=(3,))
    assert np.allclose(er.apply(vec), er.as_matrix() @ vec)

    # Test 2D rotation
    er = ERAttr(dim=2)
    er.random()
    vec = np.random.uniform(-10, 10, size=(2,))
    assert np.allclose(er.apply(vec), er.as_matrix() @ vec)
