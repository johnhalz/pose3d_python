from typing import Tuple

from attrs import define, field

from .et import ET
from .er import ER


@define
class Pose:
    position: ET = field(factory=ET, eq=True)
    orientation: ER = field(factory=ER, eq=True)
    name: str = field(default='', eq=False)

    # Setter functions
    def random(self) -> None:
        """
        Sets the position and orientation to random values.
        """
        self.orientation.random()
        self.position.random()

    def zero(self) -> None:
        """
        Sets the position vector to zero and orientation to identity.
        """
        self.orientation.identity()
        self.position.zero()

    # Getter functions
    def dims(self) -> Tuple[int, int]:
        """
        Returns the dimensions of the position and orientation (in that order).

        Returns:
        --------
        - `tuple[int, int]`: Dimension of position and orientation (in that order)
        """
        return self.position.dim, self.orientation.dim
