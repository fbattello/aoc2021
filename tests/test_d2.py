#!/usr/bin/env python3

import pkg_resources
import pytest

from aoc2021.d2 import Position, compute_position_part1, compute_position_part2


@pytest.fixture
def sample():
    return pkg_resources.resource_filename(__name__, "data/sample_d2.txt")


def test_compute_position_part1(sample):
    assert compute_position_part1(sample) == Position(15, 10, 0)


def test_compute_position_part2(sample):
    assert compute_position_part2(sample) == Position(15, 60, 10)
