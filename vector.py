from typing import Union
from math import sqrt, pi, acos
from decimal import Decimal, getcontext

getcontext().prec = 30

int_float_decimal = Union[int, float, Decimal]

class Vector(object):
    def __init__(self, coordinates) -> None:
        try:
            if not coordinates:
                raise ValueError
            if any(type(coordinate) != int_float_decimal for coordinate in coordinates) == False:
                raise TypeError
            self.coordinates = tuple(Decimal(coordinate) for coordinate in coordinates)
            self.dimensions = len(coordinates)
            self.magnitute = Decimal(sqrt(sum([x*x for x in self.coordinates])))
        
        except ValueError:
            raise ValueError('Coordinates cannot be empty')
        except TypeError:
            raise TypeError('Coordinates should be iterable and all values should be int/float')
    
    def get_unit_vector(self) -> Decimal:
        try:
            if self.magnitute == Decimal('0.0'):
                raise ZeroDivisionError
            return self * (Decimal('1.0') / self.magnitute)
        
        except ZeroDivisionError:
            raise ZeroDivisionError(f"Magnitute is zero, {self} is a zero vector.")
    
    def get_angle_with(self, v: object, in_degrees=False) -> float:
        dot_product = self * v
        angle_in_radian = acos(dot_product / (self.magnitute * v.magnitute))
        if in_degrees:
            degree_per_radian = 180. / pi
            angle_in_degree = angle_in_radian * degree_per_radian
            return round(angle_in_degree, 3)
        return round(angle_in_radian, 3)
    
    def __add__(self, v: object) -> object:
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def __sub__(self, v: object) -> object:
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, v: object) -> object:
        if isinstance(v, (int, float, Decimal)):
            v = Decimal(v)
            try:
                if v == Decimal('0.0'):
                    raise ZeroDivisionError
                new_coordinates = [Decimal(x * v) for x in self.coordinates]
                return Vector(new_coordinates)
            except ZeroDivisionError:
                raise ZeroDivisionError('Coordinates cannot be empty')
            
        elif isinstance(v, object):
                try:
                    if v.dimensions != self.dimensions:
                        raise ValueError
                    dot_product = sum([x * y for x, y in zip(self.coordinates, v.coordinates)])
                    return dot_product
                except ValueError:
                    raise ValueError('Dimensions should be equal')
    
        
    def __str__(self) -> str:
        return f'Vector: {self.coordinates}'
    
    def __eq__(self, value: object) -> bool:
        return self.coordinates == value.coordinates


v1 = Vector([1, 2, 3])
print(v1)

v2 = Vector([2.571, 8.259, 3.985])
v3 = Vector([2.571, 8.259, 3.985])
print(v2 == v3)

print(f"v2 + v3 is equal to {v2 + v3}")
print(f"v2 - v3 is equal to {v2 - v3}")
print(f"v2 * 10 is equal to {v2 * 10 }")
print(f"Dot product of two v2 and v3 is equal to {v2 * v3}")

print(f"||v2|| equals to {v2.magnitute}")
print(f"Unit vector of v2 equals to {v2.get_unit_vector()}")

print(f"Angle between two v2 and v3 is equal to {v2.get_angle_with(v3, in_degrees=True)}")