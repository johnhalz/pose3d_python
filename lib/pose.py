import numpy as np
from scipy.spatial.transform import Rotation as R

class Pose:
    def __init__(self, name: str) -> None:
        self.name = name
        self.rotation = Rotation.identity()
        self.position = np.array([0.0, 0.0, 0.0])
