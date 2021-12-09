#!/usr/bin/env python3

from __future__ import annotations

from typing import Optional
from enum import IntEnum
from dataclasses import dataclass
from math import prod
from aoc2021 import DATAPATH, SAMPLEPATH


def parse(filename: str) -> tuple[list[str], int, int]:
    with open(filename) as f:
        heightmap = f.read().splitlines()
    return heightmap, len(heightmap[0]), len(heightmap)


filename = DATAPATH.joinpath("input_d9.txt")
#filename = SAMPLEPATH.joinpath("sample_d9.txt")
heightmap, xmax, ymax = parse(filename)

class Move(IntEnum):
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3

@dataclass
class Point:
    x: int
    y: int

    @property
    def value(self) -> int:
        return int(heightmap[self.y][self.x])

    def __repr__(self):
        return f"{self.value} at ({self.x},{self.y})"

    def __lt__(self, other: Point):
        if not isinstance(other, Point):
            raise ValueError("Point expected")
        return self.value < other.value

    def __gt__(self, other: Point):
        if not isinstance(other, Point):
            raise ValueError("Point expected")
        return self.value > other.value

    def __eq__(self, other: Point):
        if not isinstance(other, Point):
            raise ValueError("Point expected")
        return self.x == other.x and self.y == other.y



    def adjacent(self, move: Move) -> Optional[Point]:
        match move:
            case Move.UP:
                return Point(self.x, self.y - 1) if self.y > 0 else None
            case Move.DOWN:
                return Point(self.x, self.y + 1) if self.y < ymax - 1 else None
            case Move.LEFT:
                return Point(self.x-1, self.y) if self.x > 0 else None
            case Move.RIGHT:
                return Point(self.x+1, self.y) if self.x < xmax - 1 else None

    def neighbours(self) -> list[Point]:
        return [x for x in [self.adjacent(m) for m in Move] if x]


def find_lowpoints() -> list[Point]:
    lowpoints: list[Point] = []
    for y, location in enumerate(heightmap):
        for x, _ in enumerate(location):
            p = Point(x, y)
            if p < min(p.neighbours()):
                lowpoints.append(p)
    return lowpoints

def buildflow(low: Point, flow: list[Point]):
    #print(f"enter buildflow(): {low=}{flow=}")
    for n in low.neighbours():
        if n > low and n.value < 9:
            if n not in flow:
                flow.append(n)
            buildflow(n, flow)


def main():

    # part 1

    lowpoints = find_lowpoints()
    risk_level = sum([x.value + 1 for x in lowpoints])
    print(risk_level)

    # part 2
    
    basinlengths: list[int] = []
    for lowpoint in lowpoints:
        basin = [lowpoint]
        buildflow(lowpoint, basin)
        basinlengths.append(len(basin))
    basinlengths.sort()
    print(prod(basinlengths[::-1][:3]))



if __name__ == "__main__":
    main()
