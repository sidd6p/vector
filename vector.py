class Vector(object):
    def __init__(self, coordinates) -> None:
        try:
            if not coordinates:
                raise ValueError
            if any(type(coordinate) != int for coordinate in coordinates):
                raise TypeError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)
        
        except ValueError:
            raise ValueError('Coordinates cannot be empty')
        except TypeError:
            raise TypeError('Coordinates should be iterable and all values should be int/float')
    
    def __add__(self, v: object) -> object:
        new_coordinates = [x + y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)
    
    def __sub__(self, v: object) -> object:
        new_coordinates = [x - y for x, y in zip(self.coordinates, v.coordinates)]
        return Vector(new_coordinates)

    def __mul__(self, v: object) -> object:
        if isinstance(v, (int, float)):
            new_coordinates = [x * v for x in self.coordinates]
            return Vector(new_coordinates)
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