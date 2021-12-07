#!/usr/bin/env python3

from collections import Counter
from aoc2021 import DATAPATH, SAMPLEPATH


class SchoolModel:
    def __init__(self, initialstate: list[int]):
        self.school = initialstate

    def next(self):
        newstate: list[int] = []
        births: int = 0
        for fishtimer in self.school:
            if fishtimer == 0:
                newfishtimer = 6
                births += 1
            else:
                newfishtimer = fishtimer - 1
            newstate.append(newfishtimer)
        newstate.extend([8] * births)
        # print(newstate)
        self.school = newstate

    def __repr__(self):
        return ",".join(map(str, self.school))

    def __len__(self):
        return len(self.school)


def parse(filename: str):
    with open(filename) as f:
        line = f.readline()
        school: list[int] = [*map(int, line.split(","))]
        return school


def naive_model(school: list[int], days: int) -> int:
    model = SchoolModel(school)
    for day in range(days):
        model.next()
    return len(model)


def counter_model(school: list[int], days: int) -> int:
    c = Counter(school)
    for day in range(days):
        for i in range(0, 9):
            c[i - 1] = c[i]
        c[8] = c[-1]  # births
        c[6] += c[8]
        c[-1] = 0
    return sum(c.values())


def main():
    filename = DATAPATH.joinpath("input_d6.txt")
    # filename = SAMPLEPATH.joinpath("sample_d6.txt")
    school = parse(filename)

    # part 1
    population = naive_model(school, 80)
    print(f"After 80 days : {population}")

    # part 2
    population = counter_model(school, 256)
    print(f"After 256 days : {population}")


if __name__ == "__main__":
    main()
