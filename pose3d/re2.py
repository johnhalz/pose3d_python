import numpy as np

class RE2:
    def __init__(self, name: str = '', angle: float = None, degrees: bool = True, matrix: np.ndarray = None) -> None:
        self.name = name
        
        if angle is None:
            if matrix is None:
                self.from_matrix(np.eye(2))
            else:
                self.from_matrix(matrix)
        else:
            self.from_euler(angle, degrees)

    # Setter functions
    def identity(self):
        self.from_matrix(np.eye(2))

    def inv(self):
        self.from_matrix(np.linalg.inv(self.as_matrix()))

    def random(self):
        self.__rotation.random()

    def from_matrix(self, matrix: np.ndarray) -> None:
        if matrix.shape == np.eye(2).shape:
            self.from_matrix(matrix)

    def from_euler(self, angle: float, degrees: bool = True) -> None:
        # Convert angle to radians (if necessary):
        if degrees:
            angle = np.deg2rad(angle)

        # Create rotation matrix from euler angle (rotated around z-axis)
        matrix = np.array([[np.cos(angle), -np.sin(angle)],
                           [np.sin(angle), np.cos(angle)]])
        self.from_matrix(matrix)

    # Getter functions
    def as_matrix(self) -> np.ndarray:
        return self.__rotation.reshape((2, 2))

    def as_euler(self, degrees: bool = True):
        angle = np.sign(self.as_matrix()[1][0])[0] * np.arccos(self.as_matrix()[0][0])

        if degrees:
            angle = np.rad2deg(angle)

        return angle

    # Computation functions
    def apply(self, input: np.ndarray) -> np.ndarray:
        return self.__rotation.apply(input)

    # Operator overloading
    def __str__(self) -> str:
        return f"RE2 - {self.name}: {self.as_euler(True)} degrees"

    def __repr__(self) -> str:
        return f"{self.as_euler(True)} degrees"

    def __eq__(self, other):
        if isinstance(other, RE2):
            return np.array_equal(self.as_matrix(), other.as_matrix())
        else:
            raise TypeError(f'Input parameter is {type(other)}, not RE2 as expected.')

    def __ne__(self, other):
        if isinstance(other, RE2):
            return not np.array_equal(self.as_matrix(), other.as_matrix())
        else:
            raise TypeError(f'Input parameter is {type(other)}, not RE2 as expected.')
    