#!/usr/bin/env python3

import pkg_resources
import pytest

from aoc2021.d9 import *


@pytest.fixture
def sample():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d9.txt")
    heightmap, xmax, ymax = parse(filename)
    return heightmap, xmax, ymax


def test_lowpoints(sample):
    lowpoints = find_lowpoints()
    assert len(lowpoints) == 4
    assert lowpoints == [
        Point(x=1, y=0),  # top-left
        Point(x=9, y=0),  # top-right
        Point(x=2, y=2),  # middle
        Point(x=6, y=4),  # bottom-right
    ]


def test_basin_topleft(sample):
    lowpoints = find_lowpoints()
    low = lowpoints[0]
    basin: list[Point] = [low]
    buildflow(low, basin)
    assert len(basin) == 3


def test_basin_topright(sample):
    lowpoints = find_lowpoints()
    low = lowpoints[1]
    basin: list[Point] = [low]
    buildflow(low, basin)
    assert len(basin) == 9


def test_basin_middle(sample):
    lowpoints = find_lowpoints()
    low = lowpoints[2]
    basin: list[Point] = [low]
    buildflow(low, basin)
    assert len(basin) == 14


def test_basin_bottomright(sample):
    lowpoints = find_lowpoints()
    low = lowpoints[3]
    basin: list[Point] = [low]
    buildflow(low, basin)
    assert len(basin) == 9
