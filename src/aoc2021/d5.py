#!/usr/bin/env python3

from dataclasses import dataclass
from aoc2021 import DATAPATH, SAMPLEPATH
import logging

logger = logging.getLogger(__name__)


@dataclass
class Point:
    x: int
    y: int


@dataclass
class Segment:
    a: Point
    b: Point

    def is_horizontal(self) -> bool:
        return self.a.y == self.b.y

    def is_vertical(self) -> bool:
        return self.a.x == self.b.x

    def is_diagonal(self) -> bool:
        dx = self.b.x - self.a.x
        dy = self.b.y - self.a.y
        return dx != 0 and abs(dx) == abs(dy)


class LinesOfVent:
    def __init__(self, size: int):
        self.grid: list[int] = [0] * size ** 2
        self.size = size

    def get(self, x: int, y: int) -> int:
        return self.grid[y * self.size + x]

    def incr(self, x: int, y: int) -> int:
        self.grid[y * self.size + x] += 1

    def overlap(self) -> int:
        return len([x for x in self.grid if x >= 2])

    def __repr__(self):
        res = ""
        for i in range(self.size):
            offset = i * self.size
            line = self.grid[offset : offset + self.size]
            res += "".join([str(x) if x > 0 else "." for x in line]) + "\n"
        return res


def parse(filename: str):
    with open(filename) as f:
        segments: list[Point] = []
        for entry in f:
            p1, p2 = entry.rstrip().replace(" ", "").split("->")
            segment = Segment(
                Point(*[int(x) for x in p1.split(",")]),
                Point(*[int(x) for x in p2.split(",")]),
            )
            segments.append(segment)
        return segments


def main():
    # filename = SAMPLEPATH.joinpath("sample_d5.txt")
    # lines = LinesOfVent(10)

    filename = DATAPATH.joinpath("input_d5.txt")
    lines = LinesOfVent(1000)

    segments: list[Segment] = parse(filename)

    hsegments = [x for x in segments if x.is_horizontal()]
    for seg in hsegments:
        logger.debug(seg)
        y = seg.a.y
        b1, b2 = (seg.a.x, seg.b.x) if seg.b.x > seg.a.x else (seg.b.x, seg.a.x)
        for x in range(b1, b2 + 1):
            lines.incr(x, y)
        # print(lines)

    vsegments = [x for x in segments if x.is_vertical()]
    for seg in vsegments:
        logger.debug(seg)
        x = seg.a.x
        b1, b2 = (seg.a.y, seg.b.y) if seg.b.y > seg.a.y else (seg.b.y, seg.a.y)
        for y in range(b1, b2 + 1):
            lines.incr(x, y)
        # print(lines)

    print("Part 1")
    # print(lines)
    print(f"{lines.overlap()=}")

    print("\n" + "-" * 32 + "\n")
    print("Part 2")

    dsegments = [x for x in segments if x.is_diagonal()]
    print(f"diagonal = {len(dsegments)}")
    for seg in dsegments:
        xrange = (
            range(seg.a.x, seg.b.x + 1)
            if seg.b.x > seg.a.x
            else range(seg.a.x, seg.b.x - 1, -1)
        )
        yrange = (
            range(seg.a.y, seg.b.y + 1)
            if seg.b.y > seg.a.y
            else range(seg.a.y, seg.b.y - 1, -1)
        )
        for x, y in zip((x for x in xrange), (y for y in yrange)):
            lines.incr(x, y)
    # print(lines)
    print(f"{lines.overlap()=}")


if __name__ == "__main__":
    main()
