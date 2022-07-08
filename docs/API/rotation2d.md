# Rotation2D Class

This class was created to mimic the capabilities of the `scipy.spatial.transform.Rotation` class for 2D usage.

## Member Variables

| Name | Type | Description |
| :--: | :--: | :---------- |
| `angle` | `float` | Float to hold rotation angle (only a single value is needed in 2D space). |

## Class Methods

| Name | Description |
| :--: | :---------- |
| `__init__` | Construction function - Set angle to 0 |
| `apply` | Apply rotation to `input_vector` |
| `inv` | Create new rotation with inverted angle (thus an inverse rotation) |
| `from_euler` | Set angles using euler angles value |
| `from_matrix` | Set angles using rotation matrix |
| `as_euler` | Return rotation as euler angle (degrees can be chosen as unit, default is radians) |
| `as_matrix` | Return rotation as rotation matrix |
| `identity` | Set rotation angle to 0 |
| `random` | Set rotation angle to random value between 0 and $2\pi$ |
| `align_vectors` | Set rotation angle to value that aligns two vectors |

| Name | Description | Code Link | Documentation Link |
| :--: | :---------- | :-------: | :----------------: |
| `numpy` | The fundamental package for scientific computing with Python | <https://github.com/numpy/numpy> | <https://numpy.org/doc/> |