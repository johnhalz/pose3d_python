# Pose Class

This page covers the `Pose` class. This class is a wrapper around the already existing [`scipy.spatial.transform.Rotation`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.transform.Rotation.html) class and the [`numpy.array`](https://numpy.org/doc/stable/reference/generated/numpy.array.html) class. The documentation for these classes can be found by clicking on their respective links.

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