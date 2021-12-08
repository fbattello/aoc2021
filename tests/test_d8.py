#!/usr/bin/env python3

import pkg_resources
import pytest

from aoc2021.d8 import *


@pytest.fixture
def sample():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d8.txt")
    entries: list[Entry] = parse(filename)
    return entries


def test_sample1():
    patterns = [
        "acedgfb",
        "cdfbe",
        "gcdfa",
        "fbcad",
        "dab",
        "cefabd",
        "cdfgeb",
        "eafb",
        "cagedb",
        "ab",
    ]
    digits = ["cdfeb", "fcadb", "cdfeb", "cdbaf"]
    segmap = find_segments(patterns)
    assert segmap == {
        "d": "a",
        "e": "b",
        "a": "c",
        "f": "d",
        "g": "e",
        "b": "f",
        "c": "g",
    }
    assert [decode(d, segmap) for d in digits] == [5, 3, 5, 3]
    assert output(digits, segmap) == 5353


def test_sample2():
    patterns = [
        "be",
        "cfbegad",
        "cbdgef",
        "fgaecd",
        "cgeb",
        "fdcge",
        "agebfd",
        "fecdb",
        "fabcd",
        "edb",
    ]
    digits = ["fdgacbe", "cefdb", "cefbgd", "gcbe"]
    segmap = find_segments(patterns)
    assert segmap == {
        "d": "a",
        "g": "b",
        "b": "c",
        "c": "d",
        "a": "e",
        "e": "f",
        "f": "g",
    }
    assert [decode(d, segmap) for d in digits] == [8, 3, 9, 4]
    assert output(digits, segmap) == 8394


def test_sample(sample: list[Entry]):
    total: int = 0
    for entry in sample:
        segmap = find_segments(entry.patterns)
        value = output(entry.digits, segmap)
        total += value   
    assert total == 61229