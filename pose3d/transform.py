from typing import Tuple, Union

from attrs import field, define
import numpy as np

from .et import ET
from .er import ER
from .pose import Pose


@define
class Transform:
    name: str = field(default='', eq=False)
    origin: str = field(default='origin', eq=False)
    destination: str = field(default='destination', eq=False)
    translation: ET = field(factory=ET)
    rotation: ER = field(factory=ER)

    # Setter functions
    def between_poses(self, origin_pose: Pose, destination_pose: Pose):
        """
        Compute transform between 2 3D poses. This instance of Transform
        will be modified to compute the transform from pose_1 to pose_2.

        Parameters:
        -----------
        - `origin_pose` (`Pose`): Origin pose
        - `destination_pose` (`Pose`): Destination pose
        """
        if origin_pose.dims() != destination_pose.dims():
            raise AttributeError(
                f'''Number of dimensions between both poses do not match:
                    pose_1.dims = {origin_pose.dims()}
                    pose_2.dims = {destination_pose.dims()}'''
            )

        # Compute rotation from origin_pose to destination_pose
        self.rotation.from_matrix(
            destination_pose.orientation.as_matrix() @ np.linalg.inv(origin_pose.orientation.as_matrix())
        )
        self.translation.vector = destination_pose.position.vector - origin_pose.position.vector

    def identity(self) -> None:
        """
        Set the transformation to zero and the rotation to identity.
        """
        self.translation.zero()
        self.rotation.identity()

    def inv(self) -> None:
        """
        Set the transformation to its inverse.
        """
        self.rotation.inv()
        self.translation.vector = -self.rotation.apply(self.translation.vector)

    def random(self) -> None:
        """
        Set a random transformation.
        """
        self.translation.random()
        self.rotation.random()

    # Getter functions
    def dims(self) -> Tuple[int, int]:
        """
        Returns the dimensions of the translation and rotation (in that order).

        Returns:
        --------
        - `tuple[int, int]`: Dimension of translation and rotation (in that order)
        """
        return self.translation.dim, self.rotation.dim

    def matrix(self, homogeneous: bool = True) -> np.ndarray:
        """
        Return the transformation matrix.

        Returns:
        --------
        - `np.ndarray`: Transformation matrix
        """
        matrix = np.eye(max(self.dims()) + 1)

        if self.origin != self.destination:
            matrix[:self.rotation.dim, :self.rotation.dim] = self.rotation.as_matrix()
            matrix[:self.translation.dim, -1] = self.translation.vector

        if not homogeneous:
            return matrix[:-1, :]

        return matrix

    # Computation functions
    def apply(self, io_element: Union[Pose, np.ndarray]) -> Union[Pose, np.ndarray]:
        """
        Apply transformation to `io`.

        Parameters:
        -----------
        - `io_element` (`Union[Pose, np.ndarray]`): Element to apply transformation to

        Returns:
        --------
        - `Union[Pose, np.ndarray]`: Output pose/vector
        """
        # If io_element is a Pose
        output = None
        if isinstance(io_element, Pose):
            output = Pose(
                position=ET(dim=io_element.position.dim),
                orientation=ER(dim=io_element.orientation.dim)
            )
            output.position.vector = io_element.position.vector
            output.orientation.from_quat(io_element.orientation.as_quat())

            output.orientation.from_matrix(np.dot(self.rotation.as_matrix(), output.orientation.as_matrix()))
            output.position.vector = self.rotation.apply(output.position.vector) + self.translation.vector

        # If io_element is a numpy vector
        if isinstance(io_element, np.ndarray):
            output = io_element.copy()
            output = self.rotation.apply(output) + self.translation.vector

        return output
