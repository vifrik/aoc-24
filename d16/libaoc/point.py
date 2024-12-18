class Point:
    __slots__ = ["x", "y"]

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def tuple(self):
        return (self.x, self.y)

    def copy(self):
        return Point(self.x, self.y)

    def rotate(self):
        return Point(-self.y, self.x)

    def rotate_ccw(self):
        return Point(self.y, -self.x)

    def __sub__(self, other):
        if isinstance(other, Point):
            return Point(self.x - other.x, self.y - other.y)
        else:
            return Point(self.x - other[0], self.y - other[1])

    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])

    def __repr__(self):
        return f"P({self.x},{self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __lt__(self, other):
        return self.x + self.y < other.x + other.y

    def __gt__(self, other):
        return self.x + self.y > other.x + other.y

    def __ne__(self, other):
        return self.x != other.x or self.y != other.y

    def __hash__(self):
        return hash(str(self))
