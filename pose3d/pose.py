from .te import TE
from .re3 import RE3
from .re2 import RE2

from .utils import valid_dim

class Pose:
    def __init__(self, name: str = '', dim: int = 3) -> None:
        self.name = name

        if valid_dim(dim):
            self.__dim = dim
            self.position = TE(dim=dim)
            if dim == 3:
                self.orientation = RE3()
            if dim == 2:
                self.orientation = RE2()

    def random(self):
        self.orientation.random()
        self.position.random()

    def zero(self):
        self.orientation.identity()
        self.position.zero()

    # Operator overloads
    def __repr__(self) -> str:
        return f'''Pose ({self.__dim}D) - {self.name}:
        Position:    {self.position.__repr__}
        Orientation: {self.orientation.__repr__}'''

    def __str__(self) -> str:
        return f'Position:    {self.position.__repr__}\nOrientation: {self.orientation.__repr__}'

    def __eq__(self, other) -> bool:
        if isinstance(other, Pose) and other.__dim == self.__dim:
            return self.orientation == other.orientation and self.position == other.position
        else:
            return False

    def __ne__(self, other) -> bool:
        if isinstance(other, Pose) and other.__dim == self.__dim:
            return self.orientation != other.orientation or self.position != other.position
        else:
            return False