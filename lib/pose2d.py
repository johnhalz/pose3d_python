import numpy as np
from rotation2d import Rotation2D

class Pose2D:
    def __init__(self, name) -> None:
        self.name = name
        self.rotation = Rotation2D()
        self.position = np.array([0.0, 0.0])