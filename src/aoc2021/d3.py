#!/usr/bin/env python3

from typing import Callable, Literal, TypeAlias
from aoc2021 import DATAPATH

bit: TypeAlias = Literal[0, 1]


class Report:
    def __init__(self, bitlength: int, log: list[int], logsize: int):
        self.bitlength: int = bitlength
        self.log: list[int] = log
        self.logsize: int = logsize
        self._ones: list[int] = None
        self._mostcommonbit: list[Literal[0, 1]] = None

    @classmethod
    def parse(cls, filename: str, bitlength: int):
        with open(filename) as f:
            log = [int(x, 2) for x in f]
        if not log:
            raise ValueError("Bad report")
        return cls(bitlength, log, logsize=len(log))

    def compute_ones(self) -> list[int]:
        """Computes a list composed of bitlength counters : each counter represents the number of ones at the given bit position.

        Example : [5, 7, 8, 5, 7]
        5 is the number of ones counted at the lowest bit pos
        7 is the number of ones counted at the highest bit pos
        """
        ones = [0] * self.bitlength
        for i in range(self.bitlength):
            for number in self.log:
                ones[i] += 1 if (0x01 << i & number) else 0
        return ones

    def compute_rates(self) -> tuple[int, int]:
        gamma: int = 0
        epsilon: int = 0
        ones = self.compute_ones()
        for i in range(self.bitlength):
            if ones[i] > self.logsize / 2:
                gamma += 1 << i
            else:
                epsilon += 1 << i
        return gamma, epsilon

    @staticmethod
    def most_common_bit_at_pos(log: list[int], pos: int) -> bit:
        count1 = len([x for x in log if x & 1 << pos])
        count0 = len(log) - count1
        return 1 if count1 >= count0 else 0

    def _compute_gazrating(self, f: Callable) -> int:
        rating = 0
        l: list[int] = self.log
        for pos in range(self.bitlength - 1, -1, -1):
            b: bit = self.most_common_bit_at_pos(l, pos)
            l = [x for x in l if f(x, pos, b)]
            if len(l) == 1:
                rating: int = l[0]
                break
        return rating

    def compute_gazratings(self) -> tuple[int, int]:
        o2 = self._compute_gazrating(lambda x, p, b: x >> p & 1 == b)
        co2 = self._compute_gazrating(lambda x, p, b: x >> p & 1 != b)
        return o2, co2

    @property
    def lifesupportrating(self):
        o2, co2 = self.compute_gazratings()
        return o2 * co2


def main():
    filename = DATAPATH.joinpath("input_d3.txt")
    report = Report.parse(filename, bitlength=12)

    print("Part 1")
    gamma, epsilon = report.compute_rates()
    print(f"{gamma=}, {epsilon=}")
    print(gamma * epsilon)

    print("-"*32)
    print("Part 2")
    o2, co2 = report.compute_gazratings()
    print(f"{o2=}, {co2=}")
    print(report.lifesupportrating)


if __name__ == "__main__":
    main()
