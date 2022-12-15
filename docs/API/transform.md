# Transform

## Description

This page covers the `Transform` class. This class is meant to represent transformations between frames and poses in 2D or 3D space. One should use this class to apply a transformation to a pose or a 2D/3D vector.

-------------------------

## Class Methods

- ### Transform.__init__

    `__init__(self, name: str, orig: str = 'origin', dest: str = 'destination', te_dim: int = 3, re_dim: int = 3) -> None`

    The `__init__` method is called when a new instance of the `Transform` class is created. It initializes all of the variables in the class and sets them to their default values.

    By default, the `self.translation` and `self.rotation` are set to zero and identity.

    **Parameters**

    - `name` (`str`): Set the name of the object (default: '')
    - `orig` (`str`): Set the name of the origin frame (default: `origin`)
    - `dest` (`str`): Set the name of the destination frame (default: `destination`)
    - `te_dim` (`int`): Set the number of dimensions of the translation element (default: `3`)
    - `re_dim` (`int`): Set the number of dimensions of the rotation element (default: `3`)

- ### Transform.between_poses

    `between_poses(self, pose_1: Pose, pose_2: Pose) -> None`

    Compute transform between 2 3D poses. This instance of Transform will be modifed to compute the transform from `pose_1` to `pose_2`.

    **Parameters**

    - `pose_1` (`Pose`): Origin pose
    - `pose_2` (`Pose`): Destination pose

- ### Transform.identity

    `identity(self) -> None`

    Set the transformation to zero and the rotation to identity.

- ### Transform.inv

    `inv(self) -> None`

    Set the transformation it's inverse.

- ### Transform.random

    `random(self) -> None`

    Set a random transformation.

- ### Transform.dims

    `dims(self) -> tuple[int, int]`

    Returns the dimensions of the translation and rotation (in that order).

    **Returns**

    - `tuple[int, int]`: Dimension of translation and rotation (in that order)

- ### Transform.matrix

    `matrix(self, homogeneous: bool = True) -> np.ndarray`

    Return the transformation matrix.

    **Returns**

    - `np.ndarray`: Transformation matrix

- ### Transform.apply

    `apply(self, io: Pose|np.ndarray) -> Pose|np.ndarray`

    Apply transformation to `io`.

    **Parameters**

    - `io` (`Pose | np.ndarray`): Element to apply transformation to

    **Returns**
    
    - `Pose|np.ndarray`: Output pose/vector