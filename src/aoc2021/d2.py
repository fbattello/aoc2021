#!/usr/bin/env python3

from dataclasses import dataclass
from typing import TypeAlias
from aoc2021 import DATAPATH

Command: TypeAlias = tuple[str, int]

@dataclass
class Position:
    horizontal: int = 0
    depth: int = 0
    aim: int = 0 # needed for part 2


def compute_position_part1(commands: list[Command]) -> Position:
    pos = Position()
    for direction, units in commands:
        match direction, units: 
            case "forward", x:
                pos.horizontal += x
            case "down", x:
                pos.depth += x
            case "up", x:
                pos.depth -= x
    return pos


def compute_position_part2(commands: list[Command]) -> Position:
    pos = Position()
    for direction, units in commands:
        match direction, units: 
            case "forward", x:
                pos.horizontal += x
                pos.depth += pos.aim * x
            case "down", x:
                pos.aim += x
            case "up", x:
                pos.aim -= x
    return pos

def parse(filename: str) -> list[Command]:
    with open(filename) as f:
        fields = [x.split() for x in f]
        commands = [(direction, int(steps)) for direction, steps in fields]
    return commands

def main():
    filename = DATAPATH.joinpath("input_d2.txt")
    commands: list[Command] = parse(filename)

    # part 1
    pos: Position = compute_position_part1(commands)
    print(pos)
    print(pos.horizontal * pos.depth)

    # part 2
    pos: Position = compute_position_part2(commands)
    print(pos)
    print(pos.horizontal * pos.depth)

if __name__ == "__main__":
    main()
