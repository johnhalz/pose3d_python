from typing import Dict

from attrs import define, field
import numpy as np


from .pose import Pose
from .transform import Transform


@define
class TransformSet:
    frames: Dict[str, Pose] = field(default={})

    def add_frame(self, frame_name: str, frame_data: Pose):
        """
        Add frame to transform set.

        Parameters:
        -----------
        - `frame_name` (`str`): Name of new frame
        - `frame_data` (`Pose`): Pose of frame
        """

        # Save new frame to self.frames
        self.frames[frame_name] = frame_data

    # Getter methods
    def frame_names(self) -> list:
        """
        Return list of frame names.

        Returns:
        --------
        - `list`: List of saved frame names
        """
        return list(self.frames.keys())

    def change_frame(self, input_element, from_frame: str, to_frame: str) -> np.ndarray:
        """
        Coordinate transformation of a pose (6D vector) from origin frame to target frame.

        A compound transformation from origin frame (defined in `from_frame` argument) to
        the target frame (defined in `to_frame` argument) is computed and applied to the
        input pose.

        Parameters:
        -----------
        - `input` (`np.ndarray`): Input pose
        - `from_frame` (`str`): Name of origin frame
        - `to_frame` (`str`): Name of target frame

        Returns:
        --------
        - `np.ndarray`: Transformed pose in target frame
        """
        # Create compound transformation
        transformation = self.__create_compound_transf(from_frame=from_frame, to_frame=to_frame)

        return transformation.apply(input_element)

    # noinspection PyUnreachableCode
    def wrench_change_frame(self, wrench: np.ndarray, from_frame: str, to_frame: str) -> np.ndarray:
        """
        Method to change frame of wrench vector.

        Method will perform simple rotation on forces (first three elements), and
        will rotate the total moments on the origin frame.

        Parameters:
        -----------
        - `wrench` (`np.ndarray`): Input wrench array
        - `from_frame` (`str`): Name of origin frame
        - `to_frame` (`str`): Name of target frame

        Returns:
        --------
        - `np.ndarray`: Transformed wrench array
        """
        # Verify input
        if np.array(wrench).shape != (6,):
            raise ValueError('TransformSet - Invalid wrench input. Shape must be (6,)')

        # Create compound transformation
        transformation = self.__create_compound_transf(from_frame=from_frame, to_frame=to_frame)

        # Transform wrench
        force_at_origin = wrench[:3]
        torque_at_origin = wrench[3:]

        unrotated_torque = torque_at_origin + np.cross(transformation.translation.vector, force_at_origin)
        torque_at_dest = transformation.rotation.apply(unrotated_torque)
        force_at_dest = transformation.rotation.apply(force_at_origin)

        return np.hstack([force_at_dest, torque_at_dest])

    def transform_matrix(self, from_frame: str, to_frame: str, homogeneous: bool = True) -> np.ndarray:
        """
        Return the transformation matrix to transform poses from origin
        frame to destination frame.

        Method will call the `__create_compound_transf()` method. Note that such a matrix
        can only be directly used for poses. Other calculations are required for wrench
        transformations.

        Parameters:
        -----------
        - `from_frame` (`str`): Name of origin frame
        - `to_frame` (`str`): Name of target frame
        - `homogeneous` (`bool`): Option if matrix should be homogeneous or not (3x4 or 4x4) (default: `True`)

        Returns:
        --------
        - `np.ndarray`: Numpy matrix
        """
        # Create compound transformation
        full_transf = self.__create_compound_transf(from_frame, to_frame)

        return full_transf.matrix(homogeneous=homogeneous)

    def __create_compound_transf(self, from_frame: str, to_frame: str) -> Transform:
        """
        Method to create compound transform between two frames.

        Parameters:
        -----------
        - `from_frame` (`str`): Name of origin frame
        - `to_frame` (`str`): Name of destination frame

        Returns:
        --------
        - `Transform`: Transform object
        """
        transformation = Transform(name=f'{from_frame}2{to_frame}', origin=from_frame, destination=to_frame)
        transformation.between_poses(origin_pose=self.frames[from_frame], destination_pose=self.frames[to_frame])

        return transformation
