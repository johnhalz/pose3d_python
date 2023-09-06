from pose3d import Pose, Transform, ER, ET

import numpy as np


def test_transform_between_poses():
    pose1 = Pose()
    pose2 = Pose()
    transform = Transform(name="test")

    # Random poses
    pose1.random()
    pose2.random()

    transform.between_poses(origin_pose=pose1, destination_pose=pose2)

    np.testing.assert_allclose(
        transform.rotation.as_matrix(),
        pose2.orientation.as_matrix() @ np.linalg.inv(pose1.orientation.as_matrix())
    )

    np.testing.assert_allclose(
        transform.translation.vector,
        pose2.position.vector - pose1.position.vector
    )


def test_transform_identity():
    transform = Transform(name="test")
    transform.random()
    transform.identity()

    np.testing.assert_allclose(transform.matrix(), np.eye(4))


def test_transform_inv():
    transform = Transform(name="test")
    transform.random()

    original_rotation = transform.rotation.as_matrix()
    original_translation = transform.translation.vector

    transform.inv()

    np.testing.assert_allclose(transform.matrix()[:3, :3], np.linalg.inv(original_rotation))
    np.testing.assert_allclose(transform.matrix()[:3, -1], -np.linalg.inv(original_rotation) @ original_translation)


def test_transform_random():
    transform = Transform(name="test")
    transform.random()

    assert isinstance(transform.rotation, ER)
    assert isinstance(transform.translation, ET)


def test_transform_dims():
    transform = Transform(name="test")
    transform.random()

    assert isinstance(transform.dims(), tuple)
    assert len(transform.dims()) == 2


def test_transform_apply_with_pose():
    pose = Pose()
    transform = Transform(name="test")
    transform.random()

    # Random pose
    pose.random()
    pose_transformed = transform.apply(pose)

    np.testing.assert_allclose(pose_transformed.position.vector,
                               transform.rotation.apply(pose.position.vector) + transform.translation.vector)
    np.testing.assert_allclose(pose_transformed.orientation.as_matrix(),
                               np.dot(transform.rotation.as_matrix(), pose.orientation.as_matrix()))


def test_transform_apply_with_ndarray():
    arr = np.random.rand(3)
    transform = Transform(name="test")
    transform.random()

    arr_transformed = transform.apply(arr)

    np.testing.assert_allclose(arr_transformed, transform.rotation.apply(arr) + transform.translation.vector)
