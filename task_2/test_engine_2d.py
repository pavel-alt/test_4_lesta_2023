import pytest
from mock import Mock

from task_2.engine_2d import Engine2D
from task_2.shapes import Triangle, Rectangle, Circle


@pytest.fixture(scope='module')
def engine_2d():
    return Engine2D()


@pytest.fixture(scope='module')
def shapes():
    types_shapes = [Triangle, Rectangle, Circle]
    return [Mock(spec=type_shape, draw=Mock()) for type_shape in types_shapes]


@pytest.fixture
def engine_2d_with_shapes(engine_2d, shapes):
    for shape in shapes:
        engine_2d.add(shape)
    return engine_2d


def test_set_color(engine_2d):
    engine_2d.set_color('red')
    assert engine_2d.color == 'red'


def test_add(engine_2d_with_shapes, shapes):
    assert all([shape in engine_2d_with_shapes.canvas for shape in shapes])


def test_draw(engine_2d_with_shapes):
    engine_2d_with_shapes.draw()
    assert all([shape.draw.called for shape in engine_2d_with_shapes.canvas])


def test_clear_canvas(engine_2d_with_shapes):
    engine_2d_with_shapes.draw()
    assert not engine_2d_with_shapes.canvas
