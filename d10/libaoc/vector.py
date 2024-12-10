from libaoc.point import Point


class Vector(Point):
    __slots__ = ["dx", "dy"]

    def __init__(self, x, y, dx=0, dy=0):
        super().__init__(x, y)
        self.dx = dx
        self.dy = dy

    def copy(self):
        return Vector(self.x, self.y, self.dx, self.dy)

    def step(self, n_steps=1, forward=True):
        if forward:
            self.x += n_steps * self.dx
            self.y += n_steps * self.dy
        else:
            self.x -= n_steps * self.dx
            self.y -= n_steps * self.dy

        return self

    def to_point(self) -> Point:
        return Point(self.x, self.y)

    def predict(self, n_steps=1, forward=True):
        return self.copy().step(n_steps, forward)

    def rotate(self, times=1):
        # rotate by 90 degrees
        for _ in range(times):
            t = self.dx
            self.dx = -self.dy
            self.dy = t

        return self

    def __str__(self) -> str:
        return f"V({self.x},{self.y},{self.dx},{self.dy})"

    def __hash__(self):
        return hash(str(self))
