from typing import Union
import attr

import numpy as np
from scipy.spatial.transform import Rotation

from .utils import ER_VALID_DIMS

def validate_rotation_dim(dim_value: int):
    '''Validate input dimension'''
    if dim_value not in ER_VALID_DIMS:
        raise ValueError(f'Input dimension {dim_value} is not accepted. Please use one of the \
            following: {ER_VALID_DIMS}.')

@attr.define
class ERAttr:
    name: str = attr.field(
        default='',
        eq=False,
        repr=True,
        validator=attr.validators.instance_of(str)
    )
    dim : int = attr.field(
        default=3,
        eq=True,
        repr=True,
        validator=validate_rotation_dim
    )
    _rotation: Rotation = attr.field(
        default=Rotation(quat=[0., 0., 0., 1.]),
        eq=True,
        repr=True
    )

    # Setter functions
    def identity(self) -> None:
        '''Set rotation to identity.'''
        self._rotation.identity()

    def inv(self) -> None:
        '''Invert rotation.'''
        self._rotation.inv()

    def random(self) -> None:
        '''Set the rotation to a random value.'''
        if self.dim == 2:
            self._rotation.from_euler('z', np.random.uniform(0, 360))

        else:
            self._rotation.random()

    def from_quat(self, quat: Union[np.ndarray, list]) -> None:
        '''
        Set the rotation from the value of the input `quat`.

        Note: This function will not work for `ER` objects that are defined in 2D space.

        Parameters
        ----------
        - `quat` (`Union[np.ndarray, list]`): Input quaternion
        '''
        if self.dim == 2:
            raise AttributeError('Unable to set 2D rotation from quaternion input.')

        self._rotation.from_quat(quat)

    def from_matrix(self, matrix: Union[np.ndarray, list]) -> None:
        '''
        Set the rotation from the value of the input `quat`.

        Parameters
        ----------
        - `matrix` (`np.ndarray`): Input rotation matrix
        '''
        matrix = np.array(matrix)
        if matrix.shape != (self.dim, self.dim):
            raise ValueError(f'Input matrix shape must be ({self.dim}, {self.dim}) when rotation \
                dimension is {self.dim}. Current input matrix shape: {matrix.shape}.')

        if self.dim == 2:
            eye_matrix = np.eye(3)
            eye_matrix[:2, :2] = matrix
            matrix = eye_matrix

        self._rotation.from_matrix(matrix)

    def from_angle_axis(self, angle_axis: Union[np.ndarray, list]) -> None:
        '''
        Set the rotation from the value of the input `angle_axis`.

        Note: This function will not work for `ER` objects that are defined in 2D space.

        Parameters
        ----------
        - `angle_axis` (`np.ndarray`): Input angle-axis vector
        '''
        if self.dim == 2:
            raise AttributeError('Unable to set 2D rotation from angle-axis input.')

        angle_axis = np.array(angle_axis)
        self._rotation.from_rotvec(angle_axis / np.linalg.norm(angle_axis))

    def from_euler(self, sequence: str = None, angles: Union[np.ndarray, list] = None,
        degrees: bool = True) -> None:
        '''
        Set the rotation from the value(s) of the inputs `sequence` and `angles`.
        The angle will be converted from degrees to radians if `degrees` is `True`.

        Parameters
        ----------
        - `sequence` (`str`): Sequence of euler angles (e.g. 'xyz', 'xy', 'zyx')
        - `angles` (`Union[np.ndarray, list]`): List of euler angles
        - `degrees` (`bool`): Set to true if input angles are in degrees (default: `True`)
        '''
        if self.dim == 3:
            if sequence is None:
                raise ValueError('Input sequence cannot be None.')

            self._rotation.from_euler(sequence, np.array(angles), degrees)

        elif self.dim == 2:
            self._rotation.from_euler('z', np.array(angles), degrees)

    # Getter functions
    def as_quat(self) -> np.ndarray:
        '''
        Return the stored `self.__rotation` member in quaternion form.

        Returns
        -------
        - `np.ndarray`: Quaternion vector
        '''
        return self._rotation.as_quat()

    def as_matrix(self) -> np.ndarray:
        '''
        Return the stored `self.__rotation` member in matrix form.

        Returns
        -------
        - `np.ndarray`: Rotation matrix
        '''
        return self._rotation.as_matrix()[:self.dim, :self.dim]

    def as_angle_axis(self, normalized: bool = True) -> np.ndarray:
        '''
        Return the stored `self.__rotation` member in angle-axis form.

        Parameters
        ----------
        - `normalized` (`bool`): Return a normalized vector (Defaults to `True`)

        Returns
        -------
        - `np.ndarray`: Angle-axis vector
        '''
        rotvec = self._rotation.as_rotvec()
        norm = np.linalg.norm(rotvec)

        if norm == 0.0:
            return rotvec

        if normalized:
            return rotvec/norm

        return rotvec

    def as_euler(self, sequence: str = None, degrees: bool = True) -> Union[np.ndarray, float]:
        '''
        Return the stored `self.__rotation` member in euler angles.

        Parameters
        ----------
        - `sequence` (`str`): Sequence in which the euler angle will be returned
        - `degrees` (`bool`): Option to return euler angles in degrees or not

        Returns
        -------
        - `Union[np.ndarray, float]`: Euler angle(s) (if self.dim = 2 then only \
            a float will be returned)
        '''
        if self.dim == 2:
            return self._rotation.as_euler('zyx', degrees)[0]

        if sequence is None:
            raise ValueError('Input sequence cannot be None.')

        return self._rotation.as_euler(sequence, degrees)

    def yaw(self, degrees: bool = True) -> float:
        '''
        Return rotation angle around the z axis.

        Note: This function will not work for 2D rotations.
            It is recommended to use `as_euler()` instead.

        Parameters
        ----------
        - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

        Returns
        -------
        - `float`: Yaw angle (in specified units)
        '''
        if self.dim == 2:
            raise AttributeError('Unable to return yaw angle of 2D rotation \
                (call as_euler() instead).')

        return self._rotation.as_euler('xyz', degrees)[2]

    def pitch(self, degrees: bool = True) -> float:
        '''
        Return rotation angle around the y axis.

        Note: This function will not work for 2D rotations.
            It is recommended to use `as_euler()` instead.

        Parameters
        ----------
        - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

        Returns
        -------
        - `float`: Pitch angle (in specified units)
        '''
        if self.dim == 2:
            raise AttributeError('Unable to return pitch angle of 2D rotation \
                (call as_euler() instead).')

        return self._rotation.as_euler('xyz', degrees)[1]

    def roll(self, degrees: bool = True) -> float:
        '''
        Return rotation angle around the x axis.

        Note: This function will not work for 2D rotations. It is recommended to use
        `as_euler()` instead.

        Parameters
        ----------
        - `degrees` (`bool`): Option to return value in degrees or radians (default: `True`)

        Returns
        -------
        - `float`: Roll angle (in specified units)
        '''
        if self.dim == 2:
            raise AttributeError('Unable to return roll angle of 2D rotation \
                (call as_euler() instead).')

        return self._rotation.as_euler('xyz', degrees)[0]

    # Computation functions
    def apply(self, input_element: Union[np.ndarray, list]) -> np.ndarray:
        '''
        The `apply` function applies this rotation to `input` vector.

        Note: The dimension of the input vector must match the set dimension of the `RE` object.

        Parameters
        ----------
        - `input` (`Union[np.ndarray, list]`): Input vector to be rotated

        Returns
        -------
        - `np.ndarray`: Rotated vector
        '''
        input_element = np.array(input_element)

        # Check shape of input
        if input_element.shape[0] != self.dim:
            raise ValueError(f'Input shape mismatch: self.dim ({self.dim}) != input.shape \
                ({input_element.shape[0]})')

        if self.dim == 2:
            input_element = np.hstack((input_element, [0]))

        result = self._rotation.apply(input_element)

        if self.dim == 2:
            return result[:2]

        return result
