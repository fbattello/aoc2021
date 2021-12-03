#!/usr/bin/env python3

import pkg_resources
import pytest

from aoc2021.d3 import Report


@pytest.fixture
def sample():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d3.txt")
    report: Report = Report.parse(filename, bitlength=5)
    return report


def test_compute_ones(sample: Report):
    ones = sample.compute_ones()
    assert ones == [5, 7, 8, 5, 7]


def test_compute_rates(sample: Report):
    assert sample.compute_rates() == (22, 9)


def test_compute_gazratings(sample: Report):
    assert sample.compute_gazratings() == (23, 10)
