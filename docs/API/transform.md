# Transform Class

The `Transform` class contains all of the requirements to transform a vector, pose or wrench to another coordinate frame.

## Member Variables

| Name | Type | Description |
| :--: | :--: | :---------- |
| `name` | `str` | Name to give to transform (must be set for every new instance). |
| `orig` | `str` | Name given to origin frame of reference. |
| `dest` | `str` | Name given to destination frame of reference. |
| `translation` | `np.ndarray` | Translation vector assigned to transformation (set to 0 at new instance). |
| `orientation` | `scipy.spatial.transform.Rotation` | Rotation class assigned to transformation (set to identity at new instance). |

## Class Methods

| Name | Description |
| :--: | :---------- |
| `print` | Print rotation and translation of transformation to console (will print rotation as euler angles in degrees). |
| `inv` | Create new transformation that is the inverse of the current transformation. |
| `apply` | Apply transformation to an `input` (can be a vector or a pose). |
| `matrix` | Return a transformation matrix of the current transformation (can be homogeneous or not - Default: `True`) |
| `random` | Assign random values to the rotation and translation elements of the transformation. |

## Requirements

| Name | Description | Code Link | Documentation Link |
| :--: | :---------- | :-------: | :----------------: |
| `numpy` | The fundamental package for scientific computing with Python | <https://github.com/numpy/numpy> | <https://numpy.org/doc/> |
| `scipy` | General management of scientific data | <https://github.com/scipy/scipy> | <https://docs.scipy.org/doc/scipy-1.8.1/> |
