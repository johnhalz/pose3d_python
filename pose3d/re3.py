import numpy as np
from scipy.spatial.transform import Rotation
from .utils import RE_TOLERANCE

class RE3:
    def __init__(self, name: str = '') -> None:
        self.name = name
        self.__rotation = Rotation(quat=[0, 0, 0, 1])

    # Setter functions
    def identity(self):
        self.__rotation = Rotation.identity()

    def inv(self):
        self.__rotation = self.__rotation.inv()

    def random(self):
        self.__rotation =  Rotation.random()

    def from_quat(self, quat: np.ndarray) -> None:
        self.__rotation = Rotation.from_quat(quat)

    def from_matrix(self, matrix: np.ndarray) -> None:
        self.__rotation = Rotation.from_matrix(matrix)

    def from_angle_axis(self, angle_axis: np.ndarray) -> None:
        self.__rotation = Rotation.from_rotvec(angle_axis)

    def from_euler(self, sequence: str, angles: list, degrees: bool = True) -> None:
        self.__rotation = Rotation.from_euler(sequence, angles, degrees)

    # Getter functions
    def as_quat(self) -> np.ndarray:
        return self.__rotation.as_quat()

    def as_matrix(self) -> np.ndarray:
        return self.__rotation.as_matrix().reshape((3, 3))

    def as_angle_axis(self) -> np.ndarray:
        return self.__rotation.as_rotvec()

    def as_euler(self, sequence: str, degrees: bool = True):
        return self.__rotation.as_euler(sequence, degrees)

    # Computation functions
    def apply(self, input: np.ndarray) -> np.ndarray:
        return self.__rotation.apply(input)

    # Operator overloading
    def __str__(self) -> str:
        return f"RE3 - {self.name}: {self.as_euler('xyz', True)} degrees"

    def __repr__(self) -> str:
        return f"{self.as_euler('xyz', True)} degrees"

    def __eq__(self, other):
        if isinstance(other, RE3):
            return np.allclose(self.as_quat(),
                               other.as_quat(),
                               rtol=RE_TOLERANCE,
                               atol=RE_TOLERANCE)
        else:
            raise TypeError(f'Input parameter is {type(other)}, not RE3 as expected.')

    def __ne__(self, other):
        if isinstance(other, RE3):
            return not np.allclose(self.as_quat(),
                                   other.as_quat(),
                                   rtol=RE_TOLERANCE,
                                   atol=RE_TOLERANCE)
        else:
            raise TypeError(f'Input parameter is {type(other)}, not RE3 as expected.')
    