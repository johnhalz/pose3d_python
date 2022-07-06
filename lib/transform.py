import numpy as np
from scipy.spatial.transform import Rotation


class Transform:
    def __init__(self, name: str, orig: str = None, dest: str = None) -> None:
        # Set strings
        self.name = name
        self.orig = orig
        self.dest = dest

        # Init translation and orientation
        self.translation = np.zeros(3)
        self.orientation = Rotation.identity()

    def print(self):
        print(self.name.title())
        print(f"Translation: {self.translation} [m]")
        print(f"Orientation: {self.orientation.as_euler('xyz', degrees=True)} [deg]")

    def inv(self):
        inv_transform = Transform()
        inv_transform.translation = -self.translation
        inv_transform.orientation = self.orientation.inv()

        return inv_transform

    def apply(self, input):
        pass

    def matrix(self, homogeneous: bool = True):
        matrix = np.eye(4)
        matrix[:3, :3] = self.orientation.as_matrix()
        matrix[:3, 3] = self.translation

        if not homogeneous:
            return matrix[:3, :]
        
        return matrix