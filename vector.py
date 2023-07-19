from typing import Union
from math import sqrt, pi, acos
from decimal import Decimal, getcontext

getcontext().prec = 30

int_float_decimal = Union[int, float, Decimal]


class Vector(object):
    """
    A class representing a vector in n-dimensional space.
    """

    def __init__(self, coordinates) -> None:
        """
        Initializes a new Vector object.

        :param coordinates: The coordinates of the vector as a list or tuple of int/float/Decimal values.
        """
        try:
            if not coordinates:
                raise ValueError
            if (
                any(type(coordinate) != int_float_decimal for coordinate in coordinates)
                == False
            ):
                raise TypeError
            self.coordinates = tuple(Decimal(coordinate) for coordinate in coordinates)
            self.dimensions = len(coordinates)
            self.magnitude = Decimal(sqrt(sum([x * x for x in self.coordinates])))

        except ValueError:
            raise ValueError("Coordinates cannot be empty")
        except TypeError:
            raise TypeError(
                "Coordinates should be iterable and all values should be int/float"
            )

    def __add__(self, v: object) -> object:
        """
        Adds two vectors.

        :param v: The vector to add.
        :return: The result of the vector addition.
        """
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __sub__(self, v: object) -> object:
        """
        Subtracts one vector from another.

        :param v: The vector to subtract.
        :return: The result of the vector subtraction.
        """
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, v: object) -> object:
        """
        Multiplies the vector by a scalar or calculates the dot product with another vector.

        :param v: The scalar value or the other vector.
        :return: The result of the multiplication.
        """
        if isinstance(v, (int, float, Decimal)):
            v = Decimal(v)
            new_coordinates = [Decimal(x * v) for x in self.coordinates]
            return Vector(new_coordinates)

        elif isinstance(v, object):
            try:
                if v.dimensions != self.dimensions:
                    raise ValueError
                dot_product = sum(
                    [x * y for x, y in zip(self.coordinates, v.coordinates)]
                )
                return dot_product
            except ValueError:
                raise ValueError("Dimensions should be equal")

    def __truediv__(self, v: object) -> object:
        """
        Divides the vector by a scalar or calculates the division with another vector.

        :param v: The scalar value or the other vector.
        :return: The result of the division.
        """
        if isinstance(v, (int, float, Decimal)):
            v = Decimal(v)
            try:
                if Decimal(v) == Decimal("0.0"):
                    raise ZeroDivisionError
                new_coordinates = [Decimal(x / v) for x in self.coordinates]
                return Vector(new_coordinates)
            except ZeroDivisionError:
                raise ZeroDivisionError("Value cannot be zero")

        elif isinstance(v, object):
            try:
                if v.dimensions != self.dimensions:
                    raise ValueError
                new_coordinates = list()
                for x, y in zip(self.coordinates, v.coordinates):
                    if Decimal(y) == Decimal(0.0):
                        raise ZeroDivisionError
                    new_coordinates.append(x / y)
                return Vector(new_coordinates)
            except ValueError:
                raise ValueError("Dimensions should be equal")
            except ZeroDivisionError:
                raise ZeroDivisionError(f"{v} has zero coordinate/s")

    def __str__(self) -> str:
        """
        Returns the string representation of the vector.

        :return: The string representation of the vector.
        """
        return f"Vector: {self.coordinates}"

    def __eq__(self, value: object) -> bool:
        """
        Checks if two vectors are equal.

        :param value: The other vector to compare.
        :return: True if the vectors are equal, False otherwise.
        """
        return self.coordinates == value.coordinates

    def is_zero(self, tolerance: float = 1e-10) -> bool:
        """
        Checks if the vector is a zero vector.

        :param tolerance: Tolerance for considering a vector as zero (default: 1e-10).
        :return: True if the vector is a zero vector, False otherwise.
        """
        return self.magnitude < tolerance

    def is_orthogonal_to(self, v: object) -> bool:
        """
        Checks if the vector is orthogonal to another vector.

        :param v: The other vector to check for orthogonality.
        :return: True if the vectors are orthogonal, False otherwise.
        """
        return (self.get_angle_with(v) == 90) or self.is_zero() or v.is_zero()

    def is_parallel_to(self, v: object) -> bool:
        """
        Checks if the vector is parallel to another vector.

        :param v: The other vector to check for parallelism.
        :return: True if the vectors are parallel, False otherwise.
        """
        return self.get_angle_with(v) == 0

    def get_unit_vector(self) -> Decimal:
        """
        Returns the unit vector of the current vector.

        :return: The unit vector of the vector.
        """
        try:
            if self.is_zero():
                raise ZeroDivisionError
            return self * (Decimal("1.0") / self.magnitude)

        except ZeroDivisionError:
            raise ZeroDivisionError(f"magnitude is zero, {self} is a zero vector.")

    def get_angle_with(self, v: object, in_degrees: bool = False) -> float:
        """
        Calculates the angle between two vectors.

        :param v: The other vector to find the angle with.
        :param in_degrees: If True, returns the angle in degrees; otherwise, returns radians.
        :return: The angle between the two vectors.
        """
        if self.is_zero() or v.is_zero():
            return 0
        dot_product = self * v
        angle_in_radian = acos(dot_product / (self.magnitude * v.magnitude))
        if in_degrees:
            degree_per_radian = 180.0 / pi
            angle_in_degree = angle_in_radian * degree_per_radian
            return round(angle_in_degree, 3)
        return round(angle_in_radian, 3)

    def get_parallel_to(self, v: object) -> object:
        """
        Returns the component of the vector parallel to another vector.

        :param v: The other vector to find the parallel component to.
        :return: The parallel component of the vector.
        """
        try:
            if v.is_zero():
                raise ZeroDivisionError
            return v.get_unit_vector() * (self * v / v.magnitude)
        except ZeroDivisionError:
            raise ZeroDivisionError(f"{v} is zero-vector")

    def get_orthogonal_to(self, v: object) -> object:
        """
        Returns the component of the vector orthogonal to another vector.

        :param v: The other vector to find the orthogonal component to.
        :return: The orthogonal component of the vector.
        """
        return self - self.get_parallel_to(v)

    def get_cross_product(self, v: object) -> object:
        """
        Calculates the cross product of two vectors.

        :param v: The other vector to calculate the cross product with.
        :return: The cross product of the two vectors.
        """
        try:
            if self.dimensions != 3 or v.dimensions != 3:
                raise ValueError
            new_coordinates = [
                self.coordinates[1] * v.coordinates[2]
                - self.coordinates[2] * v.coordinates[1],
                self.coordinates[2] * v.coordinates[0]
                - self.coordinates[0] * v.coordinates[2],
                self.coordinates[0] * v.coordinates[1]
                - self.coordinates[1] * v.coordinates[0],
            ]
            return Vector(new_coordinates)
        except ValueError:
            raise ValueError(
                f"{self, v}, both should have 3 dimension for cross-product"
            )

    def get_parallelogram_area_with(self, v: object) -> float:
        """
        Calculates the area of the parallelogram formed by the two vectors.

        :param v: The other vector to calculate the area with.
        :return: The area of the parallelogram.
        """
        return self.get_cross_product(v).magnitude

    def get_triangle_area_with(self, v: object) -> float:
        """
        Calculates the area of the triangle formed by the two vectors.

        :param v: The other vector to calculate the area with.
        :return: The area of the triangle.
        """
        return self.get_cross_product(v).magnitude / 2


# # Create two Vector objects v1 and v2
# v1 = Vector([0, 0, 1])
# v2 = Vector([1, 2, 9])

# # Print the vectors v1 and v2
# print("v1:", v1)
# print("v2:", v2)

# # Check if v1 is equal to v2 and print the result
# are_v1_and_v2_equal = v1 == v2
# print(f"Are v1 and v2 equal? {are_v1_and_v2_equal}")

# # Perform vector addition, subtraction, scalar multiplication, and dot product
# v1_plus_v2 = v1 + v2
# v1_minus_v2 = v1 - v2
# v1_times_10 = v1 * 10
# dot_product_v1_v2 = v1 * v2
# v1_by_10 = v1 / 10
# v1_divides_by_v2 = v1 / v2

# # Print the results of the operations
# print(f"v1 + v2 is equal to {v1_plus_v2}")
# print(f"v1 - v2 is equal to {v1_minus_v2}")
# print(f"v1 * 10 is equal to {v1_times_10}")
# print(f"Dot product of v1 and v2 is equal to {dot_product_v1_v2}")
# print(f"v1 / 10 is equal to {v1_by_10}")
# print(f"v1 divides by v2 is equal to {v1_divides_by_v2}")

# # Calculate the magnitude of v1 and print the result
# magnitude_v1 = v1.magnitude
# print(f"The magnitude of v1 is {magnitude_v1}")

# # Calculate the unit vector of v1 and print the result
# unit_vector_v1 = v1.get_unit_vector()
# print(f"The unit vector of v1 is {unit_vector_v1}")

# # Calculate the angle between v1 and v2 (in radians) and print the result
# angle_v1_v2_radians = v1.get_angle_with(v2, in_degrees=False)
# print(f"Angle between v1 and v2 (in radians) is equal to {angle_v1_v2_radians}")

# # Check if v1 is orthogonal and parallel to v2 and print the results
# is_orthogonal_v1_v2 = v1.is_orthogonal_to(v2)
# is_parallel_v1_v2 = v1.is_parallel_to(v2)
# print(f"Is v1 orthogonal to v2? {is_orthogonal_v1_v2}")
# print(f"Is v1 parallel to v2? {is_parallel_v1_v2}")

# # Calculate the component of v1 parallel and orthogonal to v2 and print the results
# v1_parallel_to_v2 = v1.get_parallel_to(v2)
# v1_orthogonal_to_v2 = v1.get_orthogonal_to(v2)
# print(f"V1's component parallel to v2 is {v1_parallel_to_v2}")
# print(f"V1's component orthogonal to v2 is {v1_orthogonal_to_v2}")

# # Check if v1 can be represented as the sum of its components parallel and orthogonal to v2 and print the result
# is_v1_parallel_orthogonal_to_v2 = v1 == v1_parallel_to_v2 + v1_orthogonal_to_v2
# print(
#     f"V1 = V1's component parallel to v2 + V1's component orthogonal to v2? {is_v1_parallel_orthogonal_to_v2}"
# )

# # Calculate the angle between v2 and its component parallel to v1 (in degrees) and print the result
# angle_v2_with_parallel_to_v1 = v2.get_angle_with(
#     v1.get_parallel_to(v2), in_degrees=True
# )
# print(
#     f"Angle between v2 and its component parallel to v1 (in degrees) is {angle_v2_with_parallel_to_v1}"
# )

# # Calculate the angle between v2 and its component orthogonal to v1 (in degrees) and print the result
# angle_v2_with_orthogonal_to_v1 = v2.get_angle_with(
#     v1.get_orthogonal_to(v2), in_degrees=True
# )
# print(
#     f"Angle between v2 and its component orthogonal to v1 (in degrees) is {angle_v2_with_orthogonal_to_v1}"
# )

# # Calculate the cross product of v1 and v2 and print the result
# cross_v1_v2 = v1.get_cross_product(v2)
# print(f"v1 x v2 is equal to: {cross_v1_v2}")

# # Calculate the area of the parallelogram formed by v1 and v2 and print the result
# parallelogram_area = v1.get_parallelogram_area_with(v2)
# print(f"Parallelogram area between v1 and v2 is: {parallelogram_area}")

# # Calculate the area of the triangle formed by v1 and v2 and print the result
# triangle_area = v1.get_triangle_area_with(v2)
# print(f"Triangle area between v1 and v2 is: {triangle_area}")
