import builtins

import pytest
from _pytest.mark import param
from mock import Mock, call

from task_2.shapes import Triangle, Rectangle, Circle


@pytest.mark.parametrize('params, expected_shape', [
    ([(1, 0), (3, 1), (1, 4)], Triangle(coord_1=(1, 0), coord_2=(3, 1), coord_3=(1, 4)))
])
def test_init_triangle(params, expected_shape):
    shape = Triangle(*params)
    assert shape.coord_1 == expected_shape.coord_1 and \
           shape.coord_2 == expected_shape.coord_2 and \
           shape.coord_3 == expected_shape.coord_3


@pytest.mark.parametrize('params, expected_shape', [
    ([(0, 0), 2, 5], Rectangle(corner_coord=(0, 0), side_1=2, side_2=5))
])
def test_init_rectangle(params, expected_shape):
    shape = Rectangle(*params)
    assert shape.corner_coord == expected_shape.corner_coord and \
           shape.side_1 == expected_shape.side_1 and \
           shape.side_2 == expected_shape.side_2


@pytest.mark.parametrize('params, expected_shape', [
    ([(1, 0), 3], Circle(center_coord=(1, 0), radius=3))
])
def test_init_circle(params, expected_shape):
    shape = Circle(*params)
    assert shape.center_coord == expected_shape.center_coord and \
           shape.radius == expected_shape.radius


@pytest.mark.parametrize('shape, print_arg', [
    param(
        Triangle(coord_1=(1, 0), coord_2=(3, 1), coord_3=(1, 4)),
        'Drawing red Triangle with vertices at points (1, 0), (3, 1), (1, 4)',
        id='Triangle'),
    param(
        Rectangle(corner_coord=(0, 0), side_1=2, side_2=5),
        'Drawing red Rectangle with sides 2 and 5 intersecting at a point (0, 0)',
        id='Rectangle'),
    param(
        Circle(center_coord=(1, 0), radius=3),
        'Drawing red Circle: (1, 0) with radius 3',
        id='Triangle')
])
def test_draw(shape, print_arg):
    builtins.print = Mock(print_arg)
    shape.draw('red')
    assert builtins.print.call_args == call(print_arg)
