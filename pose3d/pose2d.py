import numpy as np
from .te import TE
from .re2 import RE2

class Pose2D:
    def __init__(self, name: str = '') -> None:
        self.name = name
        self.orientation = RE2()
        self.position = TE(dim=2)

    def random(self):
        self.orientation.random()
        self.position.random()

    def zero(self):
        self.orientation.identity()
        self.position.zero()

    # Operator overloads
    def __repr__(self) -> str:
        return f'''Pose2D - {self.name}:
        Position:    {self.position.__repr__}
        Orientation: {self.orientation.__repr__}'''

    def __str__(self) -> str:
        return f'Position:    {self.position.__repr__}\nOrientation: {self.orientation.__repr__}'

    def __eq__(self, other):
        if isinstance(other, Pose2D):
            return self.orientation == other.orientation and self.position == other.position

    def __ne__(self, other):
        if isinstance(other, Pose2D):
            return self.orientation != other.orientation or self.position != other.position
