import numpy as np
from scipy.spatial.transform import Rotation

from pose import Pose


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
        # If input is 3D vector
        if type(input) is np.ndarray and np.size(input) == 3:
            return self.rotation.apply(input) + self.translation

        # If input is pose
        if type(input) is Pose:
            input.rotation = self.rotation.apply(input.rotation)
            input.position += self.translation

            return input

    def matrix(self, homogeneous: bool = True):

        matrix = np.eye(4)
        
        if self.orig != self.dest:
            matrix[:3, :3] = self.orientation.as_matrix()
            matrix[:3, 3] = self.translation

        if not homogeneous:
            return matrix[:3, :]
        
        return matrix