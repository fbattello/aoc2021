#!/usr/bin/env python3

from typing import Callable
from aoc2021 import DATAPATH, SAMPLEPATH

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3


def parse(filename: str) -> list[str]:
    with open(filename) as f:
        heightmap = f.read().splitlines()
    return heightmap, len(heightmap[0]), len(heightmap)


def main():
    filename = DATAPATH.joinpath("input_d9.txt")
    # filename = SAMPLEPATH.joinpath("sample_d9.txt")
    heightmap, xmax, ymax = parse(filename)

    move: Callable = [None] * 4
    move[UP] = lambda x, y: heightmap[y - 1][x] if y > 0 else None
    move[DOWN] = lambda x, y: heightmap[y + 1][x] if y < ymax - 1 else None
    move[LEFT] = lambda x, y: heightmap[y][x - 1] if x > 0 else None
    move[RIGHT] = lambda x, y: heightmap[y][x + 1] if x < xmax - 1 else None

    def neighbours(x, y) -> list[int]:
        return [*map(int, [n for n in [m(*(x, y)) for m in move] if n])]

    lowpoints = []
    for y, location in enumerate(heightmap):
        for x, height in enumerate(location):
            h = int(height)
            if h < min(neighbours(x, y)):
                lowpoints.append(h)

    risk_level = sum([x + 1 for x in lowpoints])
    print(risk_level)


if __name__ == "__main__":
    main()
