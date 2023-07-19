# Vector Operations Readme

This readme file provides an overview and usage instructions for the Vector class and its operations defined in the provided Python code.

## Table of Contents

1. [Introduction](#introduction)
2. [Author](#author)
3. [Technical Details](#technical-details)
4. [Use Case](#use-case)
5. [Example](#example)

## Introduction

The `Vector` class represents a vector in n-dimensional space. It supports various vector operations, including addition, subtraction, scalar multiplication, dot product, cross product, angle calculations, and more.

## Author

This code was authored by Siddhartha Purwar.

## Technical Details

The `Vector` class is designed to work with n-dimensional vectors represented as lists or tuples of int, float, or Decimal values. The class provides the following key methods:

- `__add__(self, v: object)`: Adds two vectors.
- `__sub__(self, v: object)`: Subtracts one vector from another.
- `__mul__(self, v: object)`: Multiplies the vector by a scalar or calculates the dot product with another vector.
- `__truediv__(self, v: object)`: Divides the vector by a scalar or another vector.
- `get_unit_vector(self)`: Returns the unit vector of the current vector.
- `get_angle_with(self, v: object, in_degrees=False)`: Calculates the angle between two vectors.
- `is_orthogonal_to(self, v: object)`: Checks if the vector is orthogonal to another vector.
- `is_parallel_to(self, v: object)`: Checks if the vector is parallel to another vector.
- `get_parallel_to(self, v: object)`: Returns the component of the vector parallel to another vector.
- `get_orthogonal_to(self, v: object)`: Returns the component of the vector orthogonal to another vector.
- `get_cross_product(self, v: object)`: Calculates the cross product of two vectors.
- `get_parallelogram_area_with(self, v: object)`: Calculates the area of the parallelogram formed by two vectors.
- `get_triangle_area_with(self, v: object)`: Calculates the area of the triangle formed by two vectors.

## Use Case

The `Vector` class is useful for performing various vector operations in mathematical calculations, physics simulations, computer graphics, and machine learning applications.

## Example

Below is an example of how to use the `Vector` class:

```python
# Create two Vector objects v1 and v2
v1 = Vector([0, 0, 1])
v2 = Vector([1, 2, 9])

# Perform vector addition, subtraction, scalar multiplication, and dot product
v1_plus_v2 = v1 + v2
v1_minus_v2 = v1 - v2
v1_times_10 = v1 * 10
dot_product_v1_v2 = v1 * v2

# Print the results of the operations
print(f"v1 + v2 is equal to {v1_plus_v2}")
print(f"v1 - v2 is equal to {v1_minus_v2}")
print(f"v1 * 10 is equal to {v1_times_10}")
print(f"Dot product of v1 and v2 is equal to {dot_product_v1_v2}")

# Calculate the magnitude of v1 and print the result
magnitude_v1 = v1.magnitude
print(f"The magnitude of v1 is {magnitude_v1}")

# Calculate the unit vector of v1 and print the result
unit_vector_v1 = v1.get_unit_vector()
print(f"The unit vector of v1 is {unit_vector_v1}")

# Calculate the angle between v1 and v2 (in radians) and print the result
angle_v1_v2_radians = v1.get_angle_with(v2, in_degrees=False)
print(f"Angle between v1 and v2 (in radians) is equal to {angle_v1_v2_radians}")

# Check if v1 is orthogonal and parallel to v2 and print the results
is_orthogonal_v1_v2 = v1.is_orthogonal_to(v2)
is_parallel_v1_v2 = v1.is_parallel_to(v2)
print(f"Is v1 orthogonal to v2? {is_orthogonal_v1_v2}")
print(f"Is v1 parallel to v2? {is_parallel_v1_v2}")

# Calculate the component of v1 parallel and orthogonal to v2 and print the results
v1_parallel_to_v2 = v1.get_parallel_to(v2)
v1_orthogonal_to_v2 = v1.get_orthogonal_to(v2)
print(f"V1's component parallel to v2 is {v1_parallel_to_v2}")
print(f"V1's component orthogonal to v2 is {v1_orthogonal_to_v2}")

# Check if v1 can be represented as the sum of its components parallel and orthogonal to v2 and print the result
is_v1_parallel_orthogonal_to_v2 = v1 == v1_parallel_to_v2 + v1_orthogonal_to_v2
print(
    f"V1 = V1's component parallel to v2 + V1's component orthogonal to v2? {is_v1_parallel_orthogonal_to_v2}"
)

# Calculate the angle between v2 and its component parallel to v1 (in degrees) and print the result
angle_v2_with_parallel_to_v1 = v2.get_angle_with(
    v1.get_parallel_to(v2), in_degrees=True
)
print(
    f"Angle between v2 and its component parallel to v1 (in degrees) is {angle_v2_with_parallel_to_v1}"
)

# Calculate the angle between v2 and its component orthogonal to v1 (in degrees) and print the result
angle_v2_with_orthogonal_to_v1 = v2.get_angle_with(
    v1.get_orthogonal_to(v2), in_degrees=True
)
print(
    f"Angle between v2 and its component orthogonal to v1 (in degrees) is {angle_v2_with_orthogonal_to_v1}"
)

# Calculate the cross product of v1 and v2 and print the result
cross_v1_v2 = v1.get_cross_product(v2)
print(f"v1 x v2 is equal to: {cross_v1_v2}")

# Calculate the area of the parallelogram formed by v1 and v2 and print the result
parallelogram_area = v1.get_parallelogram_area_with(v2)
print(f"Parallelogram area between v1 and v2 is: {parallelogram_area}")

# Calculate the area of the triangle formed by v1 and v2 and print the result
triangle_area = v1.get_triangle_area_with(v2)
print(f"Triangle area between v1 and v2 is: {triangle_area}")
