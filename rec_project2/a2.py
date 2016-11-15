from polygon import Polygon, find_point
import math

class Example(Polygon):
    def __init__(self, angle):
        super().__init__()
        self._angle = angle

    def get_points(self):
        start = (100, 100)
        points = [start]

        next_point = find_point(start, self._angle, 100)
        points.append(next_point)

        next_point = find_point(next_point, 1.5 * self._angle, 150)
        points.append(next_point)

        points.append((-100, -100))
        points.append((0, 100))

        return points


class Rectangle(Polygon):
    def __init__(self, short_side, long_side):
        super().__init__()
        self._short_side = short_side
        self._long_side = long_side

    def get_points(self):
        start = (0.0, 0.0)
        points = [start]

        next_point = find_point(start, 0, self._long_side)
        points.append(next_point)

        next_point = find_point(next_point, 90, self._short_side)
        points.append(next_point)

        next_point = find_point(next_point, 180, self._long_side)
        points.append(next_point)

        return points


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Triangle(Polygon):
    def __init__(self, side1, side2, angle):
        super().__init__()
        angle_rad = math.radians(angle)
        self._side1 = side1
        self._side2 = side2
        # solve for the third side using the law of cosines
        self._side3 = math.sqrt(side1**2 + side2**2 - 2 * side1 * side2 * math.cos(angle_rad))
        # solve for the angle using the law of sines
        self._angle1 = math.degrees(math.asin(math.sin(angle_rad) * side1 / self._side3))
        self._angle2 = 180 - self._angle1 - angle

    def get_points(self):
        start = (0.0, 0.0)
        points = [start]
        
        next_point = find_point(start, 0, self._side3)
        points.append(next_point)
        
        next_point = find_point(next_point, 180 - self._angle1, self._side2)
        points.append(next_point)

        next_point = find_point(next_point, 180 + self._angle2, self._side1)
        points.append(next_point)
        return points


class EquilateralTriangle(Triangle):
    def __init__(self, side):
        super().__init__(side, side, 60)

def main():
    rectangle = Rectangle(123, 211)
    rectangle.draw()

    square = Square(57)
    square.draw()

    triangle = Triangle(100, 100, 90)
    triangle.draw()

    eq_triangle = EquilateralTriangle(333)
    eq_triangle.draw()
    
if __name__ == '__main__':
    main()
