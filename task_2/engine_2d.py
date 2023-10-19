from typing import Union

from task_2.shapes import Triangle, Rectangle, Circle


class Engine2D:
    """
    Engine for drawing simple 2D primitives.
    """
    def __init__(self):
        self.canvas = []
        self.color = 'black'

    def add(self, shape: Union[Triangle, Rectangle, Circle]) -> None:
        """
        Adding shape in canvas.
        """
        self.canvas.append(shape)

    def draw(self) -> None:
        """
        Drawing all shapes from canvas and clearing it.
        """
        for shape in self.canvas:
            shape.draw(self.color)
        self.canvas.clear()

    def set_color(self, color: str) -> None:
        """
        Change shape's color.
        """
        self.color = color
