#!/usr/bin/env python3

from __future__ import annotations

import sys
from typing import Optional, Literal
from enum import IntEnum
from dataclasses import dataclass
from math import prod
from aoc2021 import DATAPATH, SAMPLEPATH


def parse(filename: str) -> list[str]:
    with open(filename) as f:
        return f.read().splitlines()


@dataclass
class Octopus:
    grid: Grid
    x: int
    y: int
    level: Literal[0, 9]
    flashes: int = 0
    flashedthisstep = False

    def __repr__(self):
        return f"{self.level} at ({self.x},{self.y})"

    def reset(self):
        self.flashedthisstep = False

    def lvlup(self) -> int:
        self.level += 1
        return self.level

    def neighbours(self) -> list[Octopus]:
        return self.grid.neighbours(self)

    def flash(self) -> bool:
        self.flashedthisstep = True
        self.flashes += 1


class Grid:
    def __init__(self, grid: list[str]):
        self.xmax = len(grid[0])
        self.ymax = len(grid)
        self.octopuses: dict[int, Octopus] = {}
        for y, levels in enumerate(grid):
            for x, level in enumerate(levels):
                self.octopuses[y * self.xmax + x] = Octopus(self, x, y, int(level))

    def __len__(self):
        return len(self.octopuses)

    def get(self, x: int, y: int):
        try:
            return self.octopuses[y * self.xmax + x]
        except KeyError as e:
            print(f"Bad index : {x=}, {y=}")

    @property
    def all(self):
        return self.octopuses.values()

    def neighbours(self, o: Octopus) -> list[Octopus]:
        xmin = max(o.x - 1, 0)
        xmax = min(o.x + 1, self.xmax - 1)
        ymin = max(o.y - 1, 0)
        ymax = min(o.y + 1, self.ymax - 1)
        octopuses: list[Octopus] = []
        for x in range(xmin, xmax + 1):
            for y in range(ymin, ymax + 1):
                if x == o.x and y == o.y:
                    continue
                octopuses.append(self.get(x, y))
        return octopuses

    def flash(self, o: Octopus):  # recursive
        if o.flashedthisstep:
            return
        o.flash()
        for n in self.neighbours(o):
            # This increases the energy level of all adjacent octopuses by 1
            n.lvlup()
            # If this causes an octopus to have an energy level greater than 9, it also flashes
            if n.level > 9:
                self.flash(n)

    def _step1(self):
        # First, the energy level of each octopus increases by 1
        for octopus in self.all:
            octopus.lvlup()

    def _step2(self):
        while True:
            # any octopus with an energy level greater than 9 flashes
            tobeflashed = [o for o in self.all if o.level > 9 and not o.flashedthisstep]
            if not tobeflashed:
                return
            for octopus in tobeflashed:
                self.flash(octopus)

    def _step3(self):
        # any octopus that flashed during this step has its energy level set to 0
        for octopus in self.all:
            if octopus.level > 9:
                octopus.level = 0

    def step(self):
        self.reset()
        self._step1()
        self._step2()
        self._step3()

    def reset(self):
        for o in self.all:
            o.reset()

    def __repr__(self):
        grid = ""
        for y in range(self.ymax):
            for x in range(self.xmax):
                lvl = self.get(x, y).level
                grid += str(self.get(x, y).level) if lvl <= 9 else "*"
            grid += "\n"
        return grid


def main():
    filename = DATAPATH.joinpath("input_d11.txt")
    # filename = SAMPLEPATH.joinpath("sample_d11.txt")

    # lines = []
    # lines.append("11111")
    # lines.append("19991")
    # lines.append("19191")
    # lines.append("19991")
    # lines.append("11111")
    # grid = Grid(lines)

    # part 1

    grid = Grid(parse(filename))
    for _ in range(100):
        grid.step()

    print(grid)
    print(sum([o.flashes for o in grid.all]))

    # part 2

    grid = Grid(parse(filename))
    for step in range(1, sys.maxsize):
        grid.step()
        if all([o.level == 0 for o in grid.all]):
            break
    print(step)


if __name__ == "__main__":
    main()
