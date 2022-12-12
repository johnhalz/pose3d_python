# RE Class

## Description

This page covers the Euclidean Rotation (`RE`) class. This class is meant to represent rotations in the 2D and 3D euclidean space. One can use this class to apply a rotation to a 3D or 2D vector. This class is also capable of handling a rotation in its different forms (quaternion, matrix, euler angles, etc.).

-------------------------

## Class Methods

- ### `__init__(self, name: str = '', dim: int = 3) -> None`

    The `__init__` function is called when a new instance of the `RE` class is created. It initializes all of the variables in the class and sets them to their default values.

    By default, the `self.__rotation` member value is set to an identity value.
    
    **Parameters**

    - `name` (`str`): Set the name of the object (default: '')
    - `dim` (`int`): Set the dimension of the vector (default: `3`)

- ### `identity(self, ) -> None`

    The `identity` function sets the `self.__rotation` member to the equivalent of an identity matrix.

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.identity()     # Set new_rotation to identity
    ```

- ### `random(self, ) -> None`

    The `random` function sets the `self.__rotation` member to a random value.

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()   # Set new_rotation to random value
    ```

- ### `inv(self, ) -> None`

    The `inv` function sets the `self.__rotation` member to its inverse.

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()   # Set new_rotation to random value
    new_rotation.inv()      # Set new_rotation to its inverse
    ```

- ### `from_quat(self, quat: np.ndarray|list) -> None`

    The `from_quat` function set the `self.__rotation` member from the value of the input `quat`.

    **Note:** This function will not work for `RE` objects that are defined in 2D space.

    **Parameters**

    - `quat` (`np.ndarray|list`): Input quaternion

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.from_quat([0, 0, 0, 1])
    ```

- ### `from_matrix(self, matrix: np.ndarray) -> None`

    The `from_matrix` function set the `self.__rotation` member from the value of the input `matrix`. The function will first check whether the input matrix dimensions are suitable for the number of dimensions set for the `RE` object.

    **Parameters**

    - `matrix` (`np.ndarray`): Input matrix

    ``` py title="Example"
    new_rotation = RE(dim=2)

    matrix = np.array([[1, 2], [2, 1]])

    new_rotation.from_matrix(matrix)
    ```

- ### `from_angle_axis(self, angle_axis: np.ndarray) -> None`

    The `from_angle_axis` function set the `self.__rotation` member from the value of the input `angle_axis`.
    
    **Note:** This function will not work for `RE` objects that are defined in 2D space.

    **Parameters**

    - `angle_axis` (`np.ndarray`): Input angle-axis vector

    ``` py title="Example"
    new_rotation = RE()
    matrix = np.array([1, 2, 3])
    new_rotation.from_angle_axis(matrix)
    ```

- ### `from_euler(self, sequence: str = None, angles: np.ndarray|list = None, degrees: bool = True) -> None`

    The `from_euler` function set the `self.__rotation` member from the value(s) of the inputs `sequence` and `angles`. The angle will be converted from degrees to radians if `degrees` is `True`.

    **Parameters**

    - `sequence` (`str`): Sequence of euler angles (e.g. `xyz`, `xy`, `zyx`)
    - `angles` (`np.ndarray|list`): List of euler angles
    - `degrees` (`bool`): Set to true if input angles are in degrees (default: `True`)

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.from_euler(sequence='xyz', angles=[30, 20, 10], degrees=True)
    ```

- ### `as_quat(self, ) -> np.ndarray`

    Return the stored `self.__rotation` member in quaternion form.

    **Returns**

    - `np.ndarray`: Quaternion vector

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()           # Set to random value
    print(new_rotation.as_quat())   # Return rotation in quaternion form
    ```

- ### `as_matrix(self, ) -> np.ndarray`

    Return the stored `self.__rotation` member in matrix form.

    **Returns**

    - `np.ndarray`: Rotation matrix

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()           # Set to random value
    print(new_rotation.as_matrix()) # Return rotation in matrix form
    ```

- ### `as_angle_axis(self, ) -> np.ndarray`

    Return the stored `self.__rotation` member in angle-axis form.

    **Returns**

    - `np.ndarray`: Angle-axis vector

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()               # Set to random value
    print(new_rotation.as_angle_axis()) # Return rotation in matrix form
    ```

- ### `as_euler(self, sequence: str = None, degrees: bool = True) -> np.ndarray|float`

    Return the stored `self.__rotation` member in euler angles.

    **Parameters**

    - `sequence` (`str`): Sequence in which the euler angle will be returned
    - `degrees` (`bool`): Option to return euler angles in degrees or not

    **Returns**

    - `np.ndarray|float`: Euler angle(s) (if `RE` is in 2D then only a float will be returned)

    ``` py title="3D Example"
    new_rotation = RE()
    new_rotation.random()                               # Set to random value
    print(new_rotation.as_euler('xy', degrees=True))    # Return rotation in matrix form
    ```

    ``` py title="2D Example"
    new_rotation = RE(dim=2)
    new_rotation.random()                       # Set to random value
    print(new_rotation.as_euler(degrees=True))  # Return rotation in matrix form
    ```

- ### `yaw(self, degrees: bool = True) -> float`

    Return rotation angle around the z axis.

    **Note:** This function will not work for 2D rotations. It is recommended to use `as_euler()` instead.

    **Parameters**

    - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

    **Returns**

    - `float`: Yaw angle (in specified units)

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()       # Set to random value
    print(new_rotation.yaw())   # Return yaw angle of rotation
    ```

- ### `pitch(self, degrees: bool = True) -> float`

    Return rotation angle around the y axis.

    **Note:** This function will not work for 2D rotations. It is recommended to use `as_euler()` instead.

    **Parameters**

    - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

    **Returns**

    - `float`: Pitch angle (in specified units)

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()       # Set to random value
    print(new_rotation.pitch()) # Return pitch angle of rotation
    ```

- ### `roll(self, degrees: bool = True) -> float`

    Return rotation angle around the x axis.

    **Note:** This function will not work for 2D rotations. It is recommended to use `as_euler()` instead.

    **Parameters**

    - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

    **Returns**

    - `float`: Roll angle (in specified units)

    ``` py title="Example"
    new_rotation = RE()
    new_rotation.random()       # Set to random value
    print(new_rotation.roll())  # Return roll angle of rotation
    ```

- ### `apply(self, input: np.ndarray|list) -> np.ndarray`

    The `apply` function applies this rotation to `input` vector.

    **Note:** The dimension of the input vector must match the set dimension of the `RE` object.

    **Parameters**

    - `input` (`np.ndarray|list`): Input vector to be rotated

    **Returns**

    - `np.ndarray`: Rotated vector

    ``` py title="Example"
    vector = np.array([2, 3, 1])
    new_rotation = RE()
    new_rotation.random()       # Set to random value
    rotated_vector = new_rotation.apply(vector)
    ```