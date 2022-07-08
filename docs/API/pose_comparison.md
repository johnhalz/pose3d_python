# Pose Comparison Class

The `PoseComparison` class allows us to compare the similarity between poses for their orientation and position.

!!! note
    This class only contains static functions, therefore the methods of this class need to be called with the class name first.

    Example:
    ``` python
    different_pose: bool = PoseComparison.different_pose(pose_1, pose_2)
    ```

## Class Methods

| Name | Description |
| :--: | :---------- |
| `different_pose` | Returns `True` if two poses are different (difference is below a given threshold). |
| `calc_difference` | Calculate the difference between two poses. |

## Requirements

| Name | Description | Code Link | Documentation Link |
| :--: | :---------- | :-------: | :----------------: |
| `numpy` | The fundamental package for scientific computing with Python | <https://github.com/numpy/numpy> | <https://numpy.org/doc/> |
| `scipy` | General management of scientific data | <https://github.com/scipy/scipy> | <https://docs.scipy.org/doc/scipy-1.8.1/> |