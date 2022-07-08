# TransformSet Class

The `TransformSet` class is created to make it easy to define multiple reference frames, and the relations between them, as to make it easy for the developer to transform between two reference frames.

## Usage
The reference frames are defined in a configuration file (toml format). An example can be found below:

!!! example "frames.toml"

    ```
    [base]
    translation = [0.0, 0.0, 0.0]   # [m]
    orientation = [0.0, 0.0, 0.0]
    orientation_type = 'euler'
    orientation_units = 'degrees'

    [acp]
    translation = [0.0011, 0.0022, -0.1903]   # [m]
    orientation = [-0.1, -0.1, -179.999]
    orientation_type = 'euler'
    orientation_units = 'degrees'
    ```

Requirements for a `TransformSet` configuration file:

- One of the reference frames **must** be marked as a `base`.
- The `orientation_type` must always be present (`orientation_units` are only needed for the types of rotation where it makes sense to define them).
- When initializing a new `TransformSet`, such a configuration file must be given as an argument.
- Consistency in the `translation` units

### Application in Code
The following short script uses the `frames.toml` file to define two reference frames and transform a vector between them:

``` python
from pose_python import TransformSet
import numpy as np

frames = TransformSet(file='frames.toml')

vector = np.array([1, 1, 1])

new_vector = frames.change_frame(input=vector, from_frame='base', to_frame='acp')
```

The significant advantage here is that we can call the reference frames by name, and can therefore perform complex transformations easily and in a single line.

## Member Variables

| Name | Type | Description |
| :--: | :--: | :---------- |
| `frame_data` | `dict` | Dictionary containing all of the data collected from the `toml` config file. |
| `frame_names` | `list` | List of all of the frames found in the config file. |
| `transformations` | `list` | List of all transformations extracted from the config file. |

## Class Methods

| Name | Description |
| :--: | :---------- |
| `__init__` | Construction function - Will read and parse the data from the config file. Config file path is required as argument. |
| `change_frame` | Apply transformation(s) to an input vector or pose. |
| `wrench_change_frame` | Apply transformation(s) to an input wrench vector (`np.ndarray` of size 6). |
| `transform_matrix` | Return transformation matrix of transformation required to pass from one frame to another. |
| `__create_compound_transf` | Combine two transformations: the first going from origin frame back to `base` frame, and another going from `base` frame to the destination frame |

## Requirements

| Name | Description | Code Link | Documentation Link |
| :--: | :---------- | :-------: | :----------------: |
| `numpy` | The fundamental package for scientific computing with Python | <https://github.com/numpy/numpy> | <https://numpy.org/doc/> |
| `scipy` | General management of scientific data | <https://github.com/scipy/scipy> | <https://docs.scipy.org/doc/scipy-1.8.1/> |
