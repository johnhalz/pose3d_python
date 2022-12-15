# Pose Class

## Description

This page covers the `Pose` class. In this documentation, a pose is defined as a description of the position *and* the orientation of an object, and can exist in 2D or 3D. Hence, the `Pose` class allows the user to handle a position and orientation in 2D or 3D, by making use of the `ET` and `ER` classes set to the respective number of dimensions.

-------------------------

## Class Methods

- ### Pose.__init__

    `__init__(self, name: str = '', dim: int = 3) -> None`

    The `__init__` method is called when a new instance of the `Pose` class is created.
    It initializes all of the variables in the class and sets them to their default values.
    
    **Parameters**
    
    - `name` (`str`): Set the name of the object (default: '')
    - `dim` (`int`): Set the dimension of the vector (default: 3)

- ### Pose.random

    `random(self) -> None`

    Sets the position and orientation to random values.

    ``` py title="Example"
    new_pose = Pose()
    new_pose.random()
    ```

- ### Pose.zero

    `zero(self) -> None`

    Sets the position vector to zero and orientation to identity.

    ``` py title="Example"
    new_pose = Pose()
    new_pose.zero()
    ```

-------------------------

## Value Extraction

To extract the raw values of the position and orientation, it is recommended to go through the `ER` and `ET` members.

``` py title="Example"
new_pose = Pose()
new_pose.random()

yaw_angle = new_pose.orientation.yaw()          # Get yaw angle
position_vector = new_pose.position.vector()    # Get position vector
```

Refer to the documentation of the `ER` and `ET` classes to become familiar with their methods.