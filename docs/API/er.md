# ER Class

## Description

This page covers the Euclidean Rotation (`ER`) class. This class is meant to represent rotations in the 2D and 3D euclidean space. One can use this class to apply a rotation to a 3D or 2D vector. This class is also capable of handling a rotation in its different forms (quaternion, matrix, euler angles, etc.).

-------------------------

## Class Methods

- ### ER.__init__

    `__init__(self, name: str = '', dim: int = 3) -> None`

    The `__init__` method is called when a new instance of the `ER` class is created. It initializes all of the variables in the class and sets them to their default values.

    By default, the `self.__rotation` member value is set to an identity value.
    
    **Parameters**

    - `name` (`str`): Set the name of the object (default: '')
    - `dim` (`int`): Set the dimension of the vector (default: `3`)

- ### ER.identity

    `identity(self) -> None`

    The `identity` method sets the `self.__rotation` member to the equivalent of an identity matrix.

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.identity()     # Set new_rotation to identity
    ```

- ### ER.random

    `random(self) -> None`

    The `random` method sets the `self.__rotation` member to a random value.

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()   # Set new_rotation to random value
    ```

- ### ER.inv

    `inv(self) -> None`

    The `inv` method sets the `self.__rotation` member to its inverse.

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()   # Set new_rotation to random value
    new_rotation.inv()      # Set new_rotation to its inverse
    ```

- ### ER.from_quat

    `from_quat(self, quat: np.ndarray|list) -> None`

    The `from_quat` method set the `self.__rotation` member from the value of the input `quat`.

    **Note:** This method will not work for `ER` objects that are defined in 2D space.

    **Parameters**

    - `quat` (`np.ndarray|list`): Input quaternion

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.from_quat([0, 0, 0, 1])
    ```

- ### ER.from_matrix

    `from_matrix(self, matrix: np.ndarray) -> None`

    The `from_matrix` method set the `self.__rotation` member from the value of the input `matrix`. The method will first check whether the input matrix dimensions are suitable for the number of dimensions set for the `ER` object.

    **Parameters**

    - `matrix` (`np.ndarray`): Input matrix

    ``` py title="Example"
    new_rotation = ER(dim=2)

    matrix = np.array([[1, 2], [2, 1]])

    new_rotation.from_matrix(matrix)
    ```

- ### ER.from_angle

    `from_angle_axis(self, angle_axis: np.ndarray) -> None`

    The `from_angle_axis` method set the `self.__rotation` member from the value of the input `angle_axis`.
    
    **Note:** This method will not work for `ER` objects that are defined in 2D space.

    **Parameters**

    - `angle_axis` (`np.ndarray`): Input angle-axis vector

    ``` py title="Example"
    new_rotation = ER()
    matrix = np.array([1, 2, 3])
    new_rotation.from_angle_axis(matrix)
    ```

- ### ER.from_euler

    `from_euler(self, sequence: str = None, angles: np.ndarray|list = None, degrees: bool = True) -> None`

    The `from_euler` method set the `self.__rotation` member from the value(s) of the inputs `sequence` and `angles`. The angle will be converted from degrees to radians if `degrees` is `True`.

    **Parameters**

    - `sequence` (`str`): Sequence of euler angles (e.g. `xyz`, `xy`, `zyx`)
    - `angles` (`np.ndarray|list`): List of euler angles
    - `degrees` (`bool`): Set to true if input angles are in degrees (default: `True`)

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.from_euler(sequence='xyz', angles=[30, 20, 10], degrees=True)
    ```

- ### ER.as_quat

    `as_quat(self) -> np.ndarray`

    Return the stored `self.__rotation` member in quaternion form.

    **Returns**

    - `np.ndarray`: Quaternion vector

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()           # Set to random value
    print(new_rotation.as_quat())   # Return rotation in quaternion form
    ```

- ### ER.as_matrix

    `as_matrix(self) -> np.ndarray`

    Return the stored `self.__rotation` member in matrix form.

    **Returns**

    - `np.ndarray`: Rotation matrix

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()           # Set to random value
    print(new_rotation.as_matrix()) # Return rotation in matrix form
    ```

- ### ER.as_angle_axis

    `as_angle_axis(self) -> np.ndarray`

    Return the stored `self.__rotation` member in angle-axis form.

    **Returns**

    - `np.ndarray`: Angle-axis vector

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()               # Set to random value
    print(new_rotation.as_angle_axis()) # Return rotation in matrix form
    ```

- ### ER.as_euler

    `as_euler(self, sequence: str = None, degrees: bool = True) -> np.ndarray|float`

    Return the stored `self.__rotation` member in euler angles.

    **Parameters**

    - `sequence` (`str`): Sequence in which the euler angle will be returned
    - `degrees` (`bool`): Option to return euler angles in degrees or not

    **Returns**

    - `np.ndarray|float`: Euler angle(s) (if `ER` is in 2D then only a float will be returned)

    ``` py title="3D Example"
    new_rotation = ER()
    new_rotation.random()                               # Set to random value
    print(new_rotation.as_euler('xy', degrees=True))    # Return rotation in matrix form
    ```

    ``` py title="2D Example"
    new_rotation = ER(dim=2)
    new_rotation.random()                       # Set to random value
    print(new_rotation.as_euler(degrees=True))  # Return rotation in matrix form
    ```

- ### ER.yaw

    `yaw(self, degrees: bool = True) -> float`

    Return rotation angle around the z axis.

    **Note:** This method will not work for 2D rotations. It is recommended to use `as_euler()` instead.

    **Parameters**

    - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

    **Returns**

    - `float`: Yaw angle (in specified units)

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()       # Set to random value
    print(new_rotation.yaw())   # Return yaw angle of rotation
    ```

- ### ER.pitch

    `pitch(self, degrees: bool = True) -> float`

    Return rotation angle around the y axis.

    **Note:** This method will not work for 2D rotations. It is recommended to use `as_euler()` instead.

    **Parameters**

    - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

    **Returns**

    - `float`: Pitch angle (in specified units)

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()       # Set to random value
    print(new_rotation.pitch()) # Return pitch angle of rotation
    ```

- ### ER.roll

    `roll(self, degrees: bool = True) -> float`

    Return rotation angle around the x axis.

    **Note:** This method will not work for 2D rotations. It is recommended to use `as_euler()` instead.

    **Parameters**

    - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

    **Returns**

    - `float`: Roll angle (in specified units)

    ``` py title="Example"
    new_rotation = ER()
    new_rotation.random()       # Set to random value
    print(new_rotation.roll())  # Return roll angle of rotation
    ```

- ### ER.apply

    `apply(self, input: np.ndarray|list) -> np.ndarray`

    The `apply` method applies this rotation to `input` vector.

    **Note:** The dimension of the input vector must match the set dimension of the `ER` object.

    **Parameters**

    - `input` (`np.ndarray|list`): Input vector to be rotated

    **Returns**

    - `np.ndarray`: Rotated vector

    ``` py title="Example"
    vector = np.array([2, 3, 1])
    new_rotation = ER()
    new_rotation.random()       # Set to random value
    rotated_vector = new_rotation.apply(vector)
    ```