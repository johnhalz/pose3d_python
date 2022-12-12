# Transform Set

## Description

This page covers `TransformSet` class. This class is meant to represent a group of transforms in 2D or 3D space. One should use this class to apply transformations to a vector or pose.

-------------------------

## Class Methods

- ### `add_frame(self, frame_name: str, frame_data: dict|Pose) -> None`

    Add frame to transform set.

    **Parameters**

    - `frame_name` (`str`): Name of new frame
    - `frame_data` (`dict | Pose`): Data of frame

- ### `frame_names(self) -> list`

    Return list of frame names.

    **Returns**
    
    - `list`: List of saved frame names

- ### `change_frame(self, input, from_frame: str, to_frame: str) -> np.ndarray`

    Coordinate transformation of a pose (6D vector) from origin frame to target frame.

    A compund transformation from origin frame (defined in `from_frame` argument) to the target frame (defined in `to_frame` argument) is computed and applied to the input pose.

    **Parameters**
    
    - `input` (`np.ndarray`): Input pose
    - `from_frame` (`str`): Name of origin frame
    - `to_frame` (`str`): Name of target frame

    **Returns**
    
    - `np.ndarray`: Transformed pose in target frame

- ### `wrench_change_frame(self, wrench: np.ndarray, from_frame: str, to_frame: str) -> np.ndarray`

    Method to change frame of wrench vector.

    Method will perform simple rotation on forces (first three elements), and will rotate the total moments on the origin frame.

    **Parameters**
    
    - `wrench` (`np.ndarray`): Input wrench array
    - `from_frame` (`str`): Name of origin frame
    - `to_frame` (`str`): Name of target frame

    **Returns**
    
    - `np.ndarray`: Transformed wrench array

- ### `transform_matrix(self, from_frame: str, to_frame: str, homogeneous: bool = True) -> np.ndarray`

    Return the transformation matrix to transform poses from origin frame to destination frame.

    Method will call the `__create_compound_transf()` method. Note that such a matrix can only be directly used for poses. Other calculations are required for wrench transformations.

    **Parameters**
    
    - `from_frame` (`str`): Name of origin frame
    - `to_frame` (`str`): Name of target frame
    - `homogeneous` (`bool`): Option if matrix should be homogenous or not (3x4 or 4x4) (default: `True`)

    **Returns**
    
    - `np.ndarray`: Numpy matrix

- ### `__create_compound_transf(self, from_frame: str, to_frame: str) -> Transform`

    Method to create compound transform between two frames.

    **Parameters**
    
    - `from_frame` (`str`): Name of origin frame
    - `to_frame` (`str`): Name of destination frame

    **Returns**
    
    - `Transform`: Transform object