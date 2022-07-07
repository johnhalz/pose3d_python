# Transformations

Transformations are vital to for almost automation project.

## Transformations & Inverse Transformations

The transformations that we handle in this library are composed of rotations and translations. They can be represented as matrix, such as the following:

$$
\underline{T} = \begin{bmatrix}
\underline{R} & \vec{t} \\
[0]_{3\times 1} & 1
\end{bmatrix}
$$

where $\underline{R}$ is the rotation matrix and $\vec{t}$ is the translation vector.

The inverse transform can be determined by the following operations on the elements of the original transformation:

$$
T^{-1} = \begin{bmatrix}
\underline{R}^{-1} & -\underline{R}\vec{t} \\
[0]_{3\times 1} & 1
\end{bmatrix}
$$

## Transforming Vectors

Transforming vectors involves the following operations below (in their order):
1. Apply rotation to vector
2. Add translation vector to rotated vector

This can of course be done be multiplying the transformation matrix by the homogeneous variation of the input vector (while other methods exist, this is the most common and easiest to understand).

## Transforming Poses

In this documentation, we define a pose $P$ as an element containing an orientation $O$ and a position $E$.

Transforming poses is similar to transforming a vector. If we want to transform a pose $P$ from frame $A$ to frame $B$ we do the following:

- Apply the transformation rotation to the orientation of the pose:
    
    $$
    O_B = R_{A\rightarrow B} O_A
    $$

- Add the transformation's translation to the position of the pose:
    
    $$
    E_B = E_A + \vec{t}_{A\rightarrow B}
    $$

## Transforming Forces & Torques

Transforming the forces and torques (also known as a wrench vector) involves different calculations than for a simple vector. Let us demonstrate the theory with example parameters.

Say we have a wrench vector in the frame $A$ ($\vec{W}_A$), and we want to transform the force and torque elements to the frame $B$. We know the transformation $T_{A\rightarrow B}$.

To transform the force $\vec{F}_A$, we just need to apply the rotation to the force vector:

$$
\vec{F}_B = R_{A\rightarrow B} \vec{F}_A
$$

To transform the torque $\vec{M}_A$, we do the following calculation:

$$
\vec{M}_B = R_{A\rightarrow B} \left[ \left(\vec{F}_A \times \vec{t}_{A\rightarrow B}\right) + \vec{M}_A \right]
$$
