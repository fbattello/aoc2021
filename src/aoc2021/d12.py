#!/usr/bin/env python3

from __future__ import annotations

import sys
from typing import Optional, Literal, TypeAlias
from enum import IntEnum
from dataclasses import dataclass
from math import prod
from aoc2021 import DATAPATH, SAMPLEPATH

CavePath: TypeAlias = list[str]

paths: list[CavePath] = []
map: dict[str, list[CavePath]] = {}


def parse(filename: str) -> dict[str, CavePath]:
    map: dict[str, CavePath] = {}
    with open(filename) as f:
        for line in f:
            a, b = line.rstrip().split("-")
            if a in map:
                map[a].append(b)
            else:
                map[a] = [b]
            if a == "start" or b == "end":
                continue
            if b in map:
                map[b].append(a)
            else:
                map[b] = [a]
        return map


def find_all_paths_dfs(graph: dict[str, list[str]], start: str, end: str, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    paths = []
    for node in graph[start]:
        if node[0].isupper() or (node[0].islower() and node not in path):
            new_paths = find_all_paths_dfs(graph, node, end, path)
            for new_path in new_paths:
                paths.append(new_path)
    return paths


def main():
    filename = DATAPATH.joinpath("input_d12.txt")
    # filename = SAMPLEPATH.joinpath("sample_d12_1.txt")

    map = parse(filename)
    paths = find_all_paths_dfs(map, "start", "end", path=[])
    print(len(paths))


if __name__ == "__main__":
    main()
