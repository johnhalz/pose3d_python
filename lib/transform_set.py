import toml
import numpy as np
from scipy.spatial.transform import Rotation
import logging as log


from sys import path
from os.path import dirname, join, abspath
path.insert(0, abspath(join(dirname(__file__), '.')))

from pose import Pose
from transform import Transform

class TransformSet:
    def __init__(self, cfg_file: str) -> None:

        self.frame_data = toml.load(cfg_file)

        # Save names of transforms
        self.frame_names = []
        for frame_name in self.frame_data.keys():
            self.frame_names.append(frame_name)

        if 'base' not in self.frame_names:
            log.error(f"Transforms - No frame is marked as base frame. Please mark one of the frames as 'base'.")
            return

        # Convert dictionary parameters to a list of transformations
        self.frames = []
        valid_rotation_types = ['euler', 'quaternion', 'rotvec', 'matrix', 'rodrigues']
        for frame_name in self.frame_data.keys():
            new_transf = Transform(name=frame_name, orig='base', dest=frame_name)
            new_transf.position = self.frame_data[frame_name]['translation']

            degree_opt = 'degree' in self.frame_data[frame_name]['orientation_units']
            orientation_type = self.frame_data[frame_name]['orientation_type']
            orientation_value = self.frame_data[frame_name]['orientation']

            if orientation_type not in valid_rotation_types:
                log.error(f"TransformSet - Invalid rotation type: {orientation_type}. Rotation type must be: {valid_rotation_types}")
                continue
            elif orientation_type == 'euler':
                new_transf.rotation = Rotation.from_euler('xyz', orientation_value, degrees=degree_opt)
            elif orientation_type == 'quaternion':
                new_transf.rotation = Rotation.from_quat(orientation_value)
            elif orientation_type == 'rotvec':
                new_transf.rotation = Rotation.from_rotvec(orientation_value, degrees=degree_opt)
            elif orientation_type == 'matrix':
                new_transf.rotation = Rotation.from_matrix(orientation_value)
            elif orientation_type == 'rodrigues':
                new_transf.rotation = Rotation.from_mrp(orientation_value)

            self.frames.append(new_transf)

    def pose_change_frame(self, pose: Pose, from_frame: str, to_frame: str):
        if from_frame not in self.frame_names or to_frame not in self.frame_names:
            log.error(f"Transforms - Invalid frame name, names must be: {self.frame_names}")
            return

        # TODO: Transform pose back to base frame from frame_1
        # TODO: Transform pose from base frame from frame_2

    def wrench_change_frame(self, wrench: np.ndarray, from_frame: str, to_frame: str):
        if from_frame not in self.frame_names or to_frame not in self.frame_names:
            log.error(f"Transforms - Invalid frame name, names must be: {self.frame_names}")
            return

        # TODO: Transform wrench back to base frame from frame_1
        # TODO: Transform wrench from base frame from frame_2

    def transform_matrix(self, from_frame: str, to_frame: str, homogeneous: bool = True):

        # TODO: Transform pose back to base frame from frame_1
        # TODO: Transform pose from base frame from frame_2
        pass
