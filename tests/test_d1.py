#!/usr/bin/env python3

import pkg_resources
import pytest

from aoc2021.d1 import parse, count_incr_steps, part1, part2


@pytest.fixture
def sample():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d1.txt")
    return parse(filename)


def test_count(sample):
    assert count_incr_steps(sample) == 7


def test_part1(sample):
    assert part1(sample) == 7


def test_part2(sample):
    assert part2(sample) == 5
