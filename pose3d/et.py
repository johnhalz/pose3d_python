from typing import Union, List

from attrs import define, field
import numpy as np

from .utils import validate_dim, to_numpy_array, validate_vector


@define
class ET:
    name: str = field(default='', eq=False)
    dim: Union[int, None] = field(default=None, validator=validate_dim, repr=False)
    vector: Union[np.ndarray, List, None] = field(default=None, converter=to_numpy_array, validator=validate_vector)

    def __attrs_post_init__(self):
        if self.vector is not None and self.dim is None:
            self.dim = self.vector.size
        elif self.vector is None and self.dim is not None:
            self.vector = np.zeros(self.dim)
        elif self.vector is None and self.dim is None:
            self.dim = 3
            self.vector = np.zeros(self.dim)

        # Optional: Validate that dim and len(vector) are consistent
        if self.vector is not None and self.dim is not None:
            if self.vector.size != self.dim:
                raise ValueError(
                    f'Inconsistent dimensions: dim is {self.dim} but vector has length {len(self.vector)}.'
                )

    @property
    def x(self) -> float:
        """
        Return the first element of the `self.__vector` member.

        Returns:
        --------
        - `float`: First element of the `self.__vector` member
        """
        return float(self.vector[0])

    @property
    def y(self) -> float:
        """
        Return the second element of the `self.__vector` member.

        Returns:
        --------
        - `float`: Second element of the `self.__vector` member
        """
        return float(self.vector[1])

    @property
    def z(self) -> float:
        """
        Return the third element of the `self.__vector` member.

        Note: This function will only work for `ET` classes set to 3 dimensions.

        Returns:
        --------
        - `float`: Third element of the `self.__vector` member
        """
        return float(self.vector[2])

    # Setter functions
    def random(self) -> None:
        """
        The `random` function sets the `self.__vector` member to a random state.
        """
        self.vector = np.random.uniform(0, 1, size=self.vector.shape)

    def zero(self) -> None:
        """
        The `zero` function sets the `self.__vector` to zero.
        """
        self.vector = np.zeros(self.dim)

    def inv(self) -> None:
        """
        The `inv` function sets the `self.__vector` member to its inverse (negative value).
        """
        self.vector = -self.vector

    def __add__(self, other):
        if isinstance(other, ET):
            if other.vector.shape == self.vector.shape:
                return ET(name=f'Sum of {self.name} and {other.name}', vector=self.vector + other.vector)

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector.shape:
                return ET(name=self.name, vector=self.vector + other)

        raise TypeError(f'Input parameter is {type(other)}, not ET or np.ndarray as expected.')

    def __sub__(self, other):
        if isinstance(other, ET):
            if other.vector.shape == self.vector.shape:
                return ET(name=f'Sum of {self.name} and {other.name}', vector=self.vector - other.vector)

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector.shape:
                return ET(name=self.name, vector=self.vector - other)

        raise TypeError(f'Input parameter is {type(other)}, not ET or np.ndarray as expected.')

    def __iadd__(self, other):
        if not isinstance(other, (ET, np.ndarray)):
            raise TypeError(f'Input parameter is {type(other)}, not ET or np.ndarray as expected.')

        if isinstance(other, ET):
            if other.vector.shape == self.vector.shape:
                self.vector = self.vector + other.vector

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector.shape:
                self.vector = self.vector + other

    def __isub__(self, other):
        if isinstance(other, ET):
            if other.vector.shape == self.vector.shape:
                self.vector = self.vector - other.vector

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector.shape:
                self.vector = self.vector - other

        raise TypeError(f'Input parameter is {type(other)}, not ET or np.ndarray as expected.')

    def __neg__(self):
        self.vector = -self.vector

    def __abs__(self):
        self.vector = abs(self.vector)
