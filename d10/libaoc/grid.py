from typing import Generator, Set, Union
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
    _grid: list[list[Datum]]
    _point_map: dict[Point, tuple[int, int]] = dict()
    _unique_vals: set[str] = set()
    _val_positions: dict[str, list[Point]] = dict()

    def __init__(self, input: str) -> None:
        self._parse(input)

    def _parse(self, input: str) -> None:
        outer = list()
        lines = input.strip().splitlines()

        self.height = len(lines)
        self.width = len(lines[0])

        for line_idx, line in enumerate(lines):
            inner = list()
            for col_idx, col in enumerate(line):
                datum = Datum(col_idx, line_idx, col)
                inner.append(datum)
                point = datum.to_point()
                self._point_map[point] = line_idx, col_idx
                self._unique_vals.add(col)
                if col not in self._val_positions:
                    self._val_positions[col] = list()
                self._val_positions[col].append(point)
            outer.append(inner)
        self._grid = outer

    def find(self, value: str) -> Union[Point, None]:
        if value in self._val_positions:
            return self._val_positions[value][0]

    def find_all(self, value: str) -> Union[list[Point], None]:
        if value in self._val_positions:
            return self._val_positions[value]

    def get_data(self) -> Generator[Datum, None, None]:
        for y in range(self.height):
            for x in range(self.width):
                yield self._grid[y][x]

    def get_yx(self) -> Generator[tuple[int, int], None, None]:
        for y in range(self.height):
            for x in range(self.width):
                yield y, x

    def get(self, point: Point) -> Datum:
        y, x = self._point_map[point]
        return self._grid[y][x]

    def set(self, point: Point, value: str) -> None:
        y, x = self._point_map[point]
        self._grid[y][x].v = value

    def get_unique_values(self) -> Set[str]:
        return self._unique_vals

    def in_range(self, point: Point) -> bool:
        _in_range_x = 0 <= point.x < self.width
        _in_range_y = 0 <= point.y < self.height
        return _in_range_x and _in_range_y

    def row(self, y) -> list[Point]:
        return [self._grid[y][p] for p in range(self.height)]

    def column(self, x) -> list[Point]:
        return [self._grid[p][x] for p in range(self.width)]

    def __str__(self) -> str:
        old_y = 0
        sb = ""
        for datum in self.get_data():
            if datum.y != old_y:
                sb += "\n"
                old_y = datum.y
            sb += datum.v
        return sb
