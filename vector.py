from typing import Union

int_float = Union[int, float]

class Vector(object):
    def __init__(self, coordinates) -> None:
        try:
            if not coordinates:
                raise ValueError
            if any(type(coordinate) != int_float for coordinate in coordinates) == False:
                raise TypeError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
            self.magnitute = pow(sum([x*x for x in self.coordinates]), .5)
        
        except ValueError:
            raise ValueError('Coordinates cannot be empty')
        except TypeError:
            raise TypeError('Coordinates should be iterable and all values should be int/float')
    
   
    def get_direction(self) -> int_float:
        try:
            if self.magnitute == 0 or self.magnitute == 0.0:
                raise ZeroDivisionError
            return self * (1 / self.magnitute)
        except ZeroDivisionError:
            raise("Magnitute is zero, it is a zero vector.")

    
    def __add__(self, v: object) -> object:
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def __sub__(self, v: object) -> object:
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, v: object) -> object:
        if isinstance(v, (int, float)):
            try:
                if v == 0 or v == 0.0:
                    raise ZeroDivisionError
                new_coordinates = [x * v for x in self.coordinates]
                return Vector(new_coordinates)
            except ZeroDivisionError:
                raise ZeroDivisionError('Coordinates cannot be empty')
        elif isinstance(v, object):
                new_coordinates = [x * y for x, y in zip(self.coordinates, v.coordinates)]
                return Vector(new_coordinates)
        
    def __str__(self) -> str:
        return f'Vector: {self.coordinates}'
    
    def __eq__(self, value: object) -> bool:
        return self.coordinates == value.coordinates


v1 = Vector([1, 2, 3])
print(v1)

v2 = Vector([3, 4, 5])
v3 = Vector([1, 2, 3])
print(v1 == v3)

v4 = v2 + v3
print(v4)

v5 = v2 - v3
print(v5)

v6 = v2 * 10 
print(v6)

v7 = v2 * v3 
print(v7)

print(v7.magnitute)
v7_unit = v7.get_direction()
print(v7_unit)