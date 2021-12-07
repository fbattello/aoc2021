#!/usr/bin/env python3

import pkg_resources
import pytest

from aoc2021.d6 import naive_model, counter_model, parse


@pytest.fixture
def sample():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d6.txt")
    school: list[int] = parse(filename)
    return school


def test_18(sample):
    assert naive_model(sample, 18) == 26
    assert counter_model(sample, 18) == 26


def test_80(sample):
    assert naive_model(sample, 80) == 5934
    assert counter_model(sample, 80) == 5934
