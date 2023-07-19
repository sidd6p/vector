from typing import Union
from math import sqrt, pi, acos, sin
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
            self.magnitute = Decimal(sqrt(sum([x * x for x in self.coordinates])))

        except ValueError:
            raise ValueError("Coordinates cannot be empty")
        except TypeError:
            raise TypeError(
                "Coordinates should be iterable and all values should be int/float"
            )

    def is_zero(self, tolerance: float = 1e-10):
        """
        Checks if the vector is a zero vector.

        :param tolerance: Tolerance for considering a vector as zero (default: 1e-10).
        :return: True if the vector is a zero vector, False otherwise.
        """
        return self.magnitute < tolerance

    def get_unit_vector(self) -> Decimal:
        """
        Returns the unit vector of the current vector.

        :return: The unit vector of the vector.
        """
        try:
            if self.is_zero():
                raise ZeroDivisionError
            return self * (Decimal("1.0") / self.magnitute)

        except ZeroDivisionError:
            raise ZeroDivisionError(f"Magnitute is zero, {self} is a zero vector.")

    def get_angle_with(self, v: object, in_degrees=False) -> float:
        """
        Calculates the angle between two vectors.

        :param v: The other vector to find the angle with.
        :param in_degrees: If True, returns the angle in degrees; otherwise, returns radians.
        :return: The angle between the two vectors.
        """
        if self.is_zero() or v.is_zero():
            return 0
        dot_product = self * v
        angle_in_radian = acos(dot_product / (self.magnitute * v.magnitute))
        if in_degrees:
            degree_per_radian = 180.0 / pi
            angle_in_degree = angle_in_radian * degree_per_radian
            return round(angle_in_degree, 3)
        return round(angle_in_radian, 3)

    def is_orthogonal_to(self, v: object) -> bool:
        """
        Checks if the vector is orthogonal to another vector.

        :param v: The other vector to check for orthogonality.
        :return: True if the vectors are orthogonal, False otherwise.
        """
        print((self.is_zero == 0))
        return (self.get_angle_with(v) == 90) or self.is_zero() or v.is_zero()

    def is_parallel_to(self, v: object) -> bool:
        """
        Checks if the vector is parallel to another vector.

        :param v: The other vector to check for parallelism.
        :return: True if the vectors are parallel, False otherwise.
        """
        return self.get_angle_with(v) == 0

    def get_parallel_to(self, v: object) -> object:
        """
        Returns the component of the vector parallel to another vector.

        :param v: The other vector to find the parallel component to.
        :return: The parallel component of the vector.
        """
        try:
            if v.is_zero():
                raise ZeroDivisionError
            return v.get_unit_vector() * (self * v / v.magnitute)
        except ZeroDivisionError:
            raise ZeroDivisionError(f"{v} is zero-vector")

    def get_orthognal_to(self, v: object) -> object:
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
        pass

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
            try:
                if v.is_zero():
                    raise ZeroDivisionError
                new_coordinates = [Decimal(x * v) for x in self.coordinates]
                return Vector(new_coordinates)
            except ZeroDivisionError:
                raise ZeroDivisionError("Coordinates cannot be empty")

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


# Create two Vector objects v2 and v3
v2 = Vector([1, 2, 3])
v3 = Vector([1, 2, 9])

# Check if v2 is equal to v3 and print the result
print(f"Are v2 and v3 equal? {v2 == v3}")

# Perform vector addition, subtraction, scalar multiplication, and dot product
v2_plus_v3 = v2 + v3
v2_minus_v3 = v2 - v3
v2_times_10 = v2 * 10
dot_product_v2_v3 = v2 * v3

# Print the results of the operations
print(f"v2 + v3 is equal to {v2_plus_v3}")
print(f"v2 - v3 is equal to {v2_minus_v3}")
print(f"v2 * 10 is equal to {v2_times_10}")
print(f"Dot product of v2 and v3 is equal to {dot_product_v2_v3}")

# Calculate the magnitude of v2 and print the result
magnitude_v2 = v2.magnitute
print(f"The magnitude of v2 is {magnitude_v2}")

# Calculate the unit vector of v2 and print the result
unit_vector_v2 = v2.get_unit_vector()
print(f"The unit vector of v2 is {unit_vector_v2}")

# Calculate the angle between v2 and v3 (in radians) and print the result
angle_v2_v3_radians = v2.get_angle_with(v3, in_degrees=False)
print(f"Angle between v2 and v3 (in radians) is equal to {angle_v2_v3_radians}")

# Check if v2 is orthogonal and parallel to v3 and print the results
is_orthogonal_v2_v3 = v2.is_orthogonal_to(v3)
is_parallel_v2_v3 = v2.is_parallel_to(v3)
print(f"Is v2 orthogonal to v3? {is_orthogonal_v2_v3}")
print(f"Is v2 parallel to v3? {is_parallel_v2_v3}")

# Calculate the component of v2 parallel and orthogonal to v3 and print the results
v2_parallel_to_v3 = v2.get_parallel_to(v3)
v2_orthogonal_to_v3 = v2.get_orthognal_to(v3)
print(f"V2's component parallel to v3 is {v2_parallel_to_v3}")
print(f"V2's component orthogonal to v3 is {v2_orthogonal_to_v3}")

# Check if v2 can be represented as the sum of its components parallel and orthogonal to v3 and print the result
is_v2_parallel_orthogonal_to_v3 = v2 == v2_parallel_to_v3 + v2_orthogonal_to_v3
print(
    f"V2 = V2's component parallel to v3 + V2's component orthogonal to v3? {is_v2_parallel_orthogonal_to_v3}"
)

# Calculate the angle between v3 and its component parallel to v2 (in degrees) and print the result
angle_v3_with_parallel_to_v2 = v3.get_angle_with(
    v2.get_parallel_to(v3), in_degrees=True
)
print(
    f"Angle between v3 and its component parallel to v2 (in degrees) is {angle_v3_with_parallel_to_v2}"
)

# Calculate the angle between v3 and its component orthogonal to v2 (in degrees) and print the result
angle_v3_with_orthogonal_to_v2 = v3.get_angle_with(
    v2.get_orthognal_to(v3), in_degrees=True
)
print(
    f"Angle between v3 and its component orthogonal to v2 (in degrees) is {angle_v3_with_orthogonal_to_v2}"
)
