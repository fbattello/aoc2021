#!/usr/bin/env python3

from dataclasses import dataclass
from collections import Counter
from aoc2021 import DATAPATH, SAMPLEPATH

@dataclass
class Entry:
    patterns: list[str]
    digits: list[str]


def parse(filename: str):
    with open(filename) as f:
        entries = []
        for line in f:
            patterns, digits = [x.strip().split(" ") for x in line.split("|")]
            entries.append(Entry(patterns, digits))
        return entries


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
    
    easy_digits: int  = 0
    for entry in entries:
        lengths = [len(x) for x in entry.digits]
        counter = Counter(lengths)
        for d in (2, 4, 3, 7): # lengths matching unique digits, respectively 1, 4, 7, 8
            easy_digits += counter[d]
    print(easy_digits)


if __name__ == "__main__":
    main()

