import numpy as np

class TE:
    def __init__(self, name: str ='', dim: int = 3, vector: np.ndarray = None) -> None:
        self.name = name

        if vector is None:
            if dim is None:
                self.__dim = 3
            else:
                self.__dim = dim
            
            self.__vector = np.zeros(self.__dim)
        else:
            self.__dim = len(vector)
            self.__vector = vector

    # Setter functions
    def random(self) -> None:
        self.from_vector(np.random.rand(self.__dim))

    def from_vector(self, vector: np.ndarray) -> None:
        if vector.shape == self.__vector.shape:
            self.__vector = vector

    def zero(self) -> None:
        self.from_vector(np.zeros(self.__dim))

    def inv(self) -> None:
        self.from_vector(-self.vector())

    # Getter functions
    def vector(self) -> np.ndarray:
        return self.__vector

    def x(self) -> float:
        if self.vector().shape[0] >= 1:
            return self.vector()[0]
        else:
            return None

    def y(self) -> float:
        if self.vector().shape[0] >= 2:
            return self.vector()[1]
        else:
            return None

    def z(self) -> float:
        if self.vector().shape[0] >= 3:
            return self.vector()[2]
        else:
            return None

    # Operator overloads
    def __str__(self) -> str:
        return f'TE{self.__dim} - {self.name}: {self.vector()}'

    def __repr__(self) -> str:
        return f'{self.vector()}'

    def __add__(self, other):
        if isinstance(other, TE):
            if other.vector().shape == self.vector().shape:
                return TE(name=f'Sum of {self.name} and {other.name}',
                          vector=self.vector() + other.vector())

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector().shape:
                return TE(name=self.name,
                           vector=self.vector() + other)

    def __sub__(self, other):
        if isinstance(other, TE):
            if other.vector().shape == self.vector().shape:
                return TE(name=f'Sum of {self.name} and {other.name}',
                          vector=self.vector() - other.vector())

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector().shape:
                return TE(name=self.name,
                           vector=self.vector() - other)

    def __iadd__(self, other):
        if isinstance(other, TE):
            if other.vector().shape == self.vector().shape:
                self.from_vector(self.vector() + other.vector())

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector().shape:
                self.from_vector(self.vector() + other)

    def __isub__(self, other):
        if isinstance(other, TE):
            if other.vector().shape == self.vector().shape:
                self.from_vector(self.vector() - other.vector())

        elif isinstance(other, np.ndarray):
            if other.shape == self.vector().shape:
                self.from_vector(self.vector() - other)

    def __eq__(self, other):
        if isinstance(other, TE):
            return np.array_equal(self.vector(), other.vector())
            
        elif isinstance(other, np.ndarray):
            return np.array_equal(self.vector(), other)

    def __ne__(self, other):
        if isinstance(other, TE):
            return not np.array_equal(self.vector(), other.vector())
            
        elif isinstance(other, np.ndarray):
            return not np.array_equal(self.vector(), other)

    def __neg__(self):
        self.from_vector(-self.vector())

    def __abs__(self):
        self.from_vector(abs(self.vector()))
