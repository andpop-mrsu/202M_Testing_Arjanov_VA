import pytest
from Triangle import Triangle
from triangle_func import IncorrectTriangleSides


class TestTriangleClass:
    def test_triangle_create(self):
        triangle = Triangle(9, 11, 13)
        assert triangle.first_side == 9
        assert triangle.second_side == 11
        assert triangle.third_side == 13

    def test_triangle_create_with_value_error(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle("a", "b", "c")

    def test_triangle_create_with_incorrect_sides(self):
        with pytest.raises(IncorrectTriangleSides):
            Triangle(1, 2, 3)

    def test_triangle_method_type_nonequilateral(self):
        assert Triangle(9, 11, 13).triangle_type() == 'nonequilateral'

    def test_triangle_method_type_equilateral(self):
        assert Triangle(9, 9, 9).triangle_type() == 'equilateral'

    def test_triangle_method_type_isosceles(self):
        assert Triangle(12, 12, 18).triangle_type() == 'isosceles'

    def test_triangle_method_perimeter(self):
        assert Triangle(9, 11, 13).perimeter() == 33
