#!/usr/bin/env python3

from aoc2021 import DATAPATH, SAMPLEPATH
import sys

def parse(filename: str):
    with open(filename) as f:
        line = f.readline()
        swarm: list[int] = [*map(int, line.split(","))]
        return swarm


def main():
    filename = DATAPATH.joinpath("input_d7.txt")
    #filename = SAMPLEPATH.joinpath("sample_d7.txt")
    swarm = parse(filename)

    # part 1

    positions = set(swarm) # bad hypothesis (luckily it worked out) : consider that target position matches existent positions
    minfuel = sys.maxsize
    for pos in positions:
        fuel = sum([abs(crab-pos) for crab in swarm])
        if fuel < minfuel:
            target, minfuel = pos, fuel

    print("Part 1")
    print(target, minfuel)

    # part 2

    barycentre = int(sum(positions) / len(positions))
    delta = 200
    minfuel = sys.maxsize
    cost = lambda n: n*(n+1)//2
    for pos in range(barycentre-delta, barycentre+delta): # this time explore all positions (around barycentre)
        fuel = sum([cost(abs(crab-pos)) for crab in swarm])
        if fuel < minfuel:
            target, minfuel = pos, fuel

    print("-" * 32)
    print("Part 2")
    print(target, minfuel)

if __name__ == "__main__":
    main()
