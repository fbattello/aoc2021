#!/usr/bin/env python3

from queue import LifoQueue
from aoc2021 import DATAPATH, SAMPLEPATH

OPENING = "([{<"
CLOSING = ")]}>"
PAIRMAP = {")": "(", "]": "[", "}": "{", ">": "<"}
SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}


def parse(filename: str):
    with open(filename) as f:
        return f.read().splitlines()


def parser(line: str) -> int:
    stack = LifoQueue()
    for token in line:
        if token in OPENING:
            # print(f"PUSH {token}")
            stack.put(token)
        elif token in CLOSING:
            # print(f"POP {token}")
            matchingtoken = stack.get()
            if PAIRMAP[token] != matchingtoken:
                return SCORE[token]
        else:
            return 0
    return 0


def main():

    filename = DATAPATH.joinpath("input_d10.txt")
    # filename = SAMPLEPATH.joinpath("sample_d10.txt")
    lines = parse(filename)

    score = sum([parser(l) for l in lines])
    print(score)


if __name__ == "__main__":
    main()
