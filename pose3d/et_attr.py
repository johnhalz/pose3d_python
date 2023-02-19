from attrs import define, field, validators

import numpy as np

from .utils import ET_VALID_DIMS

def list_to_array(lst: list):
    '''Convert list to numpy array.'''
    return np.array(lst)

def validate_vector_shape(instance, attribute, value):
    '''Validate shape of a vector for the ET class.'''
    if value.shape[0] not in ET_VALID_DIMS:
        raise ValueError("Vector shape must be (2,) or (3,)")

@define
class ETAttr:
    name: str = field(default='', eq=False, repr=True, validator=validators.instance_of(str))
    vector: np.array = field(
        default=np.zeros(shape=(3,)),
        eq=True,
        repr=True,
        validator=validate_vector_shape,
        converter=list_to_array)

    @classmethod
    def in_dim(cls, *, dim: int, name: str = ''):
        '''Init ET class with dimension value and name'''
        vector = np.zeros(shape=(dim,))
        validate_vector_shape(None, None, vector)
        return cls(name=name, vector=vector)

    @property
    def dim(self) -> int:
        '''
        Return the diemnsion of the vector.

        Returns
        -------
        - `int`: Dimension of the vector
        '''
        return self.vector.shape[0]

    @property
    def x(self) -> float:
        '''
        Return the first element of the `self.vector` member.

        Returns
        -------
        - `float`: First element of the `self.vector` member
        '''
        return float(self.vector[0])

    @property
    def y(self) -> float:
        '''
        Return the second element of the `self.vector` member.

        Returns
        -------
        - `float`: Second element of the `self.vector` member
        '''
        return float(self.vector[1])

    @property
    def z(self) -> float:
        '''
        Return the third element of the `self.__vector` member.

        Note: This function will only work for `ET` classes set to 3 dimensions.

        Returns
        -------
        - `float`: Third element of the `self.vector` member
        '''
        return float(self.vector[2])

    def zero(self) -> None:
        '''
        The `zero` function sets the `self.vector` to zero.
        '''
        self.vector = np.zeros(self.dim)

    def inv(self) -> None:
        '''
        The `inv` function sets the `self.vector` member to its inverse (negative value).
        '''
        self.vector = -self.vector

    def random(self) -> None:
        '''
        The `random` function sets the `self.vector` member to a random state.
        '''
        self.vector = np.random.uniform(size=self.vector.shape)
