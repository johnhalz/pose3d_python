# ET Class

## Description

This page covers the Euclidean Translation (`ET`) class. This class is meant to represent positions and translations in the 2D and 3D euclidean space. One can use this class to apply a translation to a 3D or 2D vector.

-------------------------

## Class Methods

- ### `__init__(self, name: str = '', dim: int = 3, vector: np.ndarray|list = None) -> None`

    The `__init__` method is called when a new instance of the `ET` class is created. It initializes all of the variables in the class and sets them to their default values.

    By default, the `self.__vector` member value is set to zero.
    
    **Parameters**

    - `name` (`str`): Set the name of the object (default: '')
    - `dim` (`int`): Set the dimension of the vector (default: `3`)
    - `vector` (`np.ndarray|list`): Set value of vector at `__init__` (default: `None`)

- ### `random(self) -> None`

    The `random` method sets the `self.__vector` member to a random state.

    ``` py title="Example"
    new_position = ET()
    new_position.random()           # Set to random value
    ```

- ### `from_vector(self, vector: np.ndarray|list) -> None`

    The `from_vector` method sets the `self.__vector` to the input vector.

    The method also checks whether the input dimension matches the class dimension.

    **Parameters**

    - `vector` (`np.ndarray|list`): Input vector

    ``` py title="Example"
    new_position = ET()
    new_position.from_vector([3, 2, 1]) # Set value from input vector/list
    ```

- ### `zero(self) -> None`

    The `zero` method sets the `self.__vector` to zero.

    ``` py title="Example"
    new_position = ET()
    new_position.random()   # Set to random value
    new_position.zero()     # Set to zero
    ```

- ### `inv(self) -> None`

    The `inv` method sets the `self.__vector` member to its inverse (negative value).

    ``` py title="Example"
    new_position = ET()
    new_position.random()   # Set to random value
    new_position.inv()      # Set to negative value of random values
    ```

- ### `vector(self) -> np.ndarray`

    Return the value of the `self.__vector` member.

    **Returns**

    - `np.ndarray`: Value of `self.__vector` member

    ``` py title="Example"
    new_position = ET()
    new_position.random()   # Set to random value
    new_position.vector()   # Return position vector
    ```

- ### `x(self) -> float`

    Return the first element of the `self.__vector` member.

    **Returns**

    - `float`: First element of the `self.__vector` member

    ``` py title="Example"
    new_position = ET()
    new_position.random()   # Set to random value
    new_position.x()        # Return first element of position vector
    ```

- ### `y(self) -> float`

    Return the second element of the `self.__vector` member.

    **Returns**

    - `float`: Second element of the `self.__vector` member

    ``` py title="Example"
    new_position = ET()
    new_position.random()   # Set to random value
    new_position.y()        # Return second element of position vector
    ```

- ### `z(self) -> float`

    Return the third element of the `self.__vector` member.

    **Note:** This method will only work for `ET` classes set to 3 dimensions.

    **Returns**

    - `float`: Third element of the `self.__vector` member

    ``` py title="Example"
    new_position = ET()
    new_position.random()   # Set to random value
    new_position.z()        # Return third element of position vector
    ```