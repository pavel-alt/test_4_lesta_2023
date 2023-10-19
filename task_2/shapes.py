from abc import abstractmethod, ABC
from typing import Tuple


class Shape(ABC):
    @abstractmethod
    def draw(self, color: str) -> None:
        pass


class Triangle(Shape):
    def __init__(self, coord_1: Tuple[int, int], coord_2: Tuple[int, int], coord_3: Tuple[int, int]):
        self.coord_1 = coord_1
        self.coord_2 = coord_2
        self.coord_3 = coord_3

    def draw(self, color: str) -> None:
        print(f'Drawing {color} {self.__class__.__name__} with '
              f'vertices at points {self.coord_1}, {self.coord_2}, {self.coord_3}')


class Rectangle(Shape):
    def __init__(self, corner_coord: Tuple[int, int], side_1: int, side_2: int):
        self.corner_coord = corner_coord
        self.side_1 = side_1
        self.side_2 = side_2

    def draw(self, color: str) -> None:
        print(f'Drawing {color} {self.__class__.__name__} with sides {self.side_1} and {self.side_2} '
              f'intersecting at a point {self.corner_coord}')


class Circle(Shape):
    def __init__(self, center_coord: Tuple[int, int], radius: int):
        self.center_coord = center_coord
        self.radius = radius

    def draw(self, color: str) -> None:
        print(f'Drawing {color} {self.__class__.__name__}: {self.center_coord} with radius {self.radius}')
