#!/usr/bin/env python3

import pkg_resources
from aoc2021.d12 import *


def test_first():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d12_1.txt")
    map = parse(filename)
    paths = find_all_paths_dfs(map, "start", "end", path=[])
    assert len(paths) == 10


def test_slightl_larger():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d12_2.txt")
    map = parse(filename)
    paths = find_all_paths_dfs(map, "start", "end", path=[])
    assert len(paths) == 19


def test_even_larger():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d12_3.txt")
    map = parse(filename)
    paths = find_all_paths_dfs(map, "start", "end", path=[])
    assert len(paths) == 226
