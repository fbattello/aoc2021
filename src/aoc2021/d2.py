#!/usr/bin/env python3

from dataclasses import dataclass
from aoc2021 import DATAPATH


@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0 # needed for part 2

def compute_position_part1(filename: str) -> Position:
    pos = Position()
    with open(filename) as f:
        for command in f:
            direction, steps = command.split()
            match direction, steps: 
                case "forward", x:
                    pos.horizontal += int(x)
                case "down", x:
                    pos.depth += int(x)
                case "up", x:
                    pos.depth -= int(x)
    return pos

def compute_position_part2(filename: str) -> Position:
    pos = Position()
    with open(filename) as f:
        for command in f:
            direction, steps = command.split()
            match direction, steps: 
                case "forward", x:
                    x = int(x)
                    pos.horizontal += x
                    pos.depth += pos.aim * x
                case "down", x:
                    pos.aim += int(x)
                case "up", x:
                    pos.aim -= int(x)
    return pos

def main():
    filename = DATAPATH.joinpath("input_d2.txt")

    # part 1
    pos: Position = compute_position_part1(filename)
    print(pos)
    print(pos.horizontal * pos.depth)

    # part 2
    pos: Position = compute_position_part2(filename)
    print(pos)
    print(pos.horizontal * pos.depth)

if __name__ == "__main__":
    main()
