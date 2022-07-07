# Comparing Poses

Comparing poses might sound like a simple task at first, however in practice it can get quite complicated. The `PoseComparison` class contains a static method to help solve these problems.

## Comparing Translations

Comparing translations is a simple task as it just involves two 3-dimensional vectors that can be subtracted to determine the difference between them.

## Comparing Rotations

Comparing rotations involves more thought than rotations. Let us use an example to help guide us through this process. The way we choose to represent this difference is as an angle on a sphere.

Say we have two rotations $R_1$ and $R_2$. As with all 3D rotations, there are many ways to describe/represent them:

- [Euler Angles](https://en.wikipedia.org/wiki/Euler_angles)
- [Quaternion](https://en.wikipedia.org/wiki/Quaternion)
- [3$\times$3 Matrix](https://en.wikipedia.org/wiki/Rotation_matrix#In_three_dimensions)
- [Rodrigues Vector](https://en.wikipedia.org/wiki/Rodrigues%27_rotation_formula)


A good way to determine the compound rotation between $R_1$ and $R_2$ is to multiply the matrix of one by the inverted matrix of the other:

$$
M_{\text{compound}} = M_1^{-1} M_2
$$

To determine the angle on the sphere that separate these two rotations, we can take norm of the Rodrigues representation of the compound rotation, as that defines the angle of the compound rotation between the two rotations:

$$
\text{Value} = \|\vec{r}_{\text{compound}} \|
$$

This value can then be compared with a threshold (close to zero) to determine if $R_1$ and $R_2$ are different or not.