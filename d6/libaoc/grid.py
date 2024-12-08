from typing import Union
from libaoc.point import Point


class Datum(Point):
    def __init__(self, x, y, v) -> None:
        super().__init__(x, y)
        self.v = v

    def to_point(self) -> Point:
        return Point(self.x, self.y)

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)


class Grid:
    grid: list[list[Datum]]
    point_map: dict[Point, tuple[int, int]] = {}

    def __init__(self, input: str) -> None:
        self._parse(input)

    def _parse(self, input: str):
        outer = list()
        lines = input.strip().splitlines()

        self.height = len(lines)
        self.width = len(lines[0])

        for line_idx, line in enumerate(lines):
            inner = list()
            for col_idx, col in enumerate(line):
                datum = Datum(col_idx, line_idx, col)
                inner.append(datum)
                self.point_map[datum.to_point()] = line_idx, col_idx
            outer.append(inner)
        self.grid = outer

    def find(self, value: str) -> Union[Datum, None]:
        for point in self.get_data():
            if point.v == value:
                return point
        return None

    def get_data(self):
        for y in range(self.height):
            for x in range(self.width):
                yield self.grid[y][x]

    def get_yx(self):
        for y in range(self.height):
            for x in range(self.width):
                yield y, x

    def get(self, point: Point) -> Datum:
        y, x = self.point_map[point]
        return self.grid[y][x]

    def set(self, point: Point, value: str) -> None:
        y, x = self.point_map[point]
        self.grid[y][x].v = value

    def in_range(self, point: Point) -> bool:
        _in_range_x = 0 <= point.x < self.width
        _in_range_y = 0 <= point.y < self.height
        return _in_range_x and _in_range_y

    def row(self, y) -> list[Point]:
        return [self.grid[y][p] for p in range(self.height)]

    def column(self, x):
        return [self.grid[p][x] for p in range(self.width)]

    def __str__(self) -> str:
        old_y = 0
        sb = ""
        for datum in self.get_data():
            if datum.y != old_y:
                sb += "\n"
                old_y = datum.y
            sb += datum.v
        return sb
