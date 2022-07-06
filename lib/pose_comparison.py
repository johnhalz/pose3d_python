import numpy as np

from pose import Pose, Rotation
from pose2d import Pose2D


class PoseComparison:
    @staticmethod
    def different_pose(pose_1, pose_2) -> bool:
        if not pose_1.rotation.as_matrix() == pose_2.rotation.as_matrix():
            return False

        if not pose_1.position == pose_2.position:
            return False

        return True


    @staticmethod
    def calc_difference(pose_1, pose_2, degrees: bool = False):
        position_difference = np.subtract(pose_1.position, pose_2.position)

        if type(pose_1) is Pose2D and type(pose_2) is Pose2D:
            rotation_difference = abs(pose_1.rotation.as_euler(degrees) - pose_2.rotation.as_euler(degrees))
        elif type(pose_1) is Pose and type(pose_2) is Pose:
            mat = pose_1.rotation.inv.as_matrix() @ pose_2.rotation.as_matrix()
            compound_rot = Rotation.from_matrix(mat)
            rotation_difference = np.linalg.norm(compound_rot.as_rotvec(degrees=degrees))

        return position_difference, rotation_difference