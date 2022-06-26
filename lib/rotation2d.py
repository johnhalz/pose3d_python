import numpy as np
import logging as log
from math import pi, cos, sin
from random import uniform


class Rotation2D:
    def __init__(self) -> None:
        self.angle = 0.0    # Value is stored in radians

    def apply(self, input_vector: np.array) -> np.ndarray:
        if not np.size(input_vector) == 2:
            log.error(f"Rotation2D - Incorrect input size: {np.size(input_vector)}. Vector must be dimension 2.")
            return

        result = self.as_matrix().dot(input_vector)
        return result

    def inv(self):
        self.angle = -self.angle

    def from_euler(self, value: float, degree: bool):
        if degree:
            self.angle = np.deg2rad(value)
        else:
            self.angle = value

    def from_matrix(self, matrix: np.array):
        dummy_vector = np.array([1.0, 0.0])
        self.align_vectors(dummy_vector, matrix.dot(dummy_vector))

    def as_euler(self, degree: bool) -> float:
        if degree:
            return np.rad2deg(self.angle)
        else:
            return self.angle

    def as_matrix(self) -> np.ndarray:
        matrix = [[cos(self.angle), -sin(self.angle)],
                  [sin(self.angle), cos(self.angle)]]

        return np.array(matrix)

    def identity(self):
        self.angle = 0.0

    def random(self):
        self.angle = uniform((0.0, 2.0*pi))

    def align_vectors(self, a: np.array, b: np.array):
        inner = np.inner(a, b)
        norms = np.linalg.norm(a) * np.linalg.norm(b)

        cos = inner / norms
        self.angle = np.arccos(np.clip(cos, -1.0, 1.0))     # Compute angle in radians
