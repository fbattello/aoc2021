#!/usr/bin/env python3

from dataclasses import dataclass
from collections import Counter
from aoc2021 import DATAPATH, SAMPLEPATH

LENMATCH: dict = {2: 1, 3: 7, 4: 4, 7: 8}
SEG7 = [
    "abcefg",  # 0
    "cf",  # 1
    "acdeg",  # 2
    "acdfg",  # 3
    "bcdf",  # 4
    "abdfg",  # 5
    "abdefg",  # 6
    "acf",  # 7
    "abcdefg",  # 8
    "abcdfg",  # 9
]


@dataclass
class Entry:
    patterns: list[str]
    digits: list[str]


knownlength = lambda x: LENMATCH.get(len(x))


def parse(filename: str):
    with open(filename) as f:
        entries = []
        for line in f:
            patterns, digits = [x.strip().split(" ") for x in line.split("|")]
            entries.append(Entry(patterns, digits))
        return entries


def part1(entries: list[Entry]) -> int:
    easy_digits: int = 0
    for entry in entries:
        lengths = [len(x) for x in entry.digits]
        counter = Counter(lengths)
        for d in (
            2,
            4,
            3,
            7,
        ):  # lengths matching unique digits, respectively 1, 7, 4, 8
            easy_digits += counter[d]
    return easy_digits


def find_segments(patterns: list[str]) -> dict:
    digitmap = {}
    for i in range(10):
        digitmap[i] = None

    segmap = {}
    for c in "abcdefg":
        segmap[c] = None

    for i, pattern in enumerate(patterns):
        if digit := knownlength(pattern):
            digitmap[digit] = pattern

    counter = Counter()
    for pattern in patterns:
        for segment in pattern:
            counter[segment] += 1

    # segment f OFF only in digit 2
    segmentF = [x for x, y in counter.items() if y == 9][0]
    segmap["f"] = segmentF
    digitmap[2] = [p for p in patterns if segmentF not in p][0]  # update digitmap

    segmap["a"] = [*set(digitmap[7]) - set(digitmap[1])][0]
    segmap["c"] = [*set(digitmap[2]) & set(digitmap[1])][0]
    segmap["d"] = [*set(digitmap[2]) & set(digitmap[4]) - set(segmap["c"])][0]

    # now figured out a, c, d, f
    # try to guess new numbers

    set_acdf = {segmap["a"], segmap["c"], segmap["d"], segmap["f"]}
    p6on = [p for p in patterns if len(p) == 6]  # 0, 6 and 9 have 6 segments ON
    digitmap[9] = [p for p in p6on if len(set(p) - set_acdf) == 2][0]

    # segment b left unknown in digit 4
    set_cdf = {segmap["c"], segmap["d"], segmap["f"]}
    segmap["b"] = [*set(digitmap[4]) - set_cdf][0]

    # segment g left unknown in digit 9
    set_abcdf = {segmap["a"], segmap["b"], segmap["c"], segmap["d"], segmap["f"]}
    segmap["g"] = [*set(digitmap[9]) - set_abcdf][0]

    # segment e left unknown in digit 2
    set_acdg = {segmap["a"], segmap["c"], segmap["d"], segmap["g"]}
    segmap["e"] = [*set(digitmap[2]) - set_acdg][0]

    return {v:k for k, v in segmap.items()}


def decode(digit: str, segmap: dict = None) -> int:
    if segmap:
        dst = "".join(sorted([segmap[c] for c in digit]))
    else:
        dst = digit
    return SEG7.index(dst)


def output(digits: list[str], segmap: dict = None) -> int:
    if len(digits) > 4:
        raise ValueError()
    output: int = 0
    factor: int = 1000
    for digit in digits:
        output += decode(digit, segmap) * factor
        factor //= 10
    return output


def part2(entries: list[Entry]) -> int:
    total: int = 0
    for entry in entries:
        segmap = find_segments(entry.patterns)
        value = output(entry.digits, segmap)
        total += value
    return total


def main():
    # number of segments displayed for each digit
    # '0' : 6
    # '1' : 2
    # '2' : 5
    # '3' : 5
    # '4' : 4
    # '5' : 5
    # '6' : 6
    # '7': 3
    # '8': 7
    # '9': 6

    filename = DATAPATH.joinpath("input_d8.txt")
    #filename = SAMPLEPATH.joinpath("sample_d8.txt")
    entries = parse(filename)

    # part 1

    easy_digits = part1(entries)
    print(easy_digits)

    # part 2

    total = part2(entries)
    print(total)


if __name__ == "__main__":
    main()
