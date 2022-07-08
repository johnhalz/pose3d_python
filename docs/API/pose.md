# Pose Class

This page covers the `Pose` and `Pose2D` class. For the 3D `Pose` class, this class is a wrapper around the following:

- `scipy.spatial.transform.Rotation` [Documentation Link](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html)
- `numpy.array` [Documentation Link](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

The 2D `Pose2D` class is a wrapper around the following:

- `pose_python.Rotation2D`
- `numpy.array` [Documentation Link](https://numpy.org/doc/stable/reference/generated/numpy.array.html)

The documentation for these classes can be found by clicking on their respective links.

## Member Variables

| Name | Type | Description |
| :--: | :--: | :---------- |
| `name` | `str` | String to hold the name of the pose. This variable must be set when a new instance of the class is created. |
| `position` | `numpy.ndarray` | 3D array meant to to hold the position element of the pose. |
| `rotation` | `scipy.spatial.transform.Rotation` | Rotation element meant to hold the orientation of the pose. |

## Class Methods

| Name | Description |
| :--: | :---------- |
| `__init__` | Constructor function: Requires name to be set, will set the position to [0, 0, 0] and the rotation to identity. |
| `print` | Print the elements of the pose to the console (will print the rotation in euler angles). |
| `random` | Set the position and rotation to random (mostly used for testing purposes). |

## Requirements

| Name | Description | Code Link | Documentation Link |
| :--: | :---------- | :-------: | :----------------: |
| `numpy` | The fundamental package for scientific computing with Python | <https://github.com/numpy/numpy> | <https://numpy.org/doc/> |
| `scipy` | General management of scientific data | <https://github.com/scipy/scipy> | <https://docs.scipy.org/doc/scipy-1.8.1/> |
