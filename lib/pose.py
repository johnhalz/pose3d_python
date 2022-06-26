import numpy as np
from scipy.spatial.transform import Rotation as R

class Pose:
    def __init__(self) -> None:
        self.rotation = R.identity()
        self.position = np.array([0.0, 0.0, 0.0])
