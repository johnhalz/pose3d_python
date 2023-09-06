from typing import List, Optional

import numpy as np


def validate_dim(instance, attribute, value):
    class_name = instance.__class__.__name__

    if value is None:
        return

    if not isinstance(value, int):
        raise ValueError(f"{class_name}: {attribute.name} must be an integer, got {type(value)} instead.")

    if value not in [2, 3]:
        raise ValueError(f"{class_name}: {attribute.name} must be either 2 or 3, got {value} instead.")


def to_numpy_array(value: Optional[List]) -> Optional[np.ndarray]:
    if value is None:
        return None
    return np.array(value)


def validate_vector(instance, attribute, value):
    class_name = instance.__class__.__name__
    if value is None:
        return

    if not isinstance(value, (np.ndarray, list)):
        raise ValueError(f"{class_name}: {attribute.name} must be a list or a numpy array, got {type(value)} instead.")

    # Convert list to numpy array
    if isinstance(value, list):
        value = np.array(value)

    # Optionally, check the shape
    if len(value.shape) != 1:
        raise ValueError(f"{class_name}: {attribute.name} must be 1-dimensional, got shape {value.shape} instead.")

    # Check that the length of the vector matches the `dim` attribute if it's not None
    if instance.dim is not None and value.size != instance.dim:
        raise ValueError(
            f"{class_name}: {attribute.name} attribute ({len(value)}) must match the 'dim' attribute ({instance.dim})."
        )
