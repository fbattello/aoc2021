#!/usr/bin/env python3

from more_itertools import windowed
from aoc2021 import DATAPATH

def parse(filename: str) -> list[int]:
    with open(filename) as f:
        depths = [*map(int, f)]
        return depths


def count_incr_steps(values: list[int]) -> int:
    if len(values) < 2:
        return 0
    res: int = 0
    prev: int = values[0]
    for x in values[1:]:
        if x > prev:
            res += 1
        prev = x
    return res


def part1(depths: list[int]) -> int:
    return count_incr_steps(depths)


def part2(depths: list[int]) -> int:
    windows = [sum(x) for x in windowed(depths, 3)]
    return count_incr_steps(windows)


def main():

    depths = parse(DATAPATH.joinpath("input_d1.txt"))

    increased = part1(depths)
    print(increased)

    increased = part2(depths)
    print(increased)


if __name__ == "__main__":
    main()
