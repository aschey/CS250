from polygon import Polygon, find_point

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
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

class Triangle(Polygon):
    def __init__(self, side1, side2, angle):
        super().__init__()
        self._side1 = side1
        self._side2 = side2
        self_angle = angle

    def get_points(self):
        start = (0.0, 0.0)
        points = [start]

        next_point = find_point(start, 

def main():
    #a = Example(101)
    #a.draw()

    #b = Example(201)
    #b.draw()
    a = Square(100)
    a.draw()


if __name__ == '__main__':
    main()
