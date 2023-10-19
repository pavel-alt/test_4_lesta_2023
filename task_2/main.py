from task_2.engine_2d import Engine2D
from task_2.shapes import Rectangle, Circle, Triangle

if __name__ == '__main__':
    engine_2d = Engine2D()

    engine_2d.add(Triangle(coord_1=(1, 0), coord_2=(3, 1), coord_3=(1, 4)))
    engine_2d.draw()

    engine_2d.set_color('green')

    engine_2d.add(Rectangle(corner_coord=(0, 0), side_1=2, side_2=5))
    engine_2d.add(Circle(center_coord=(1, 0), radius=3))
    engine_2d.draw()
