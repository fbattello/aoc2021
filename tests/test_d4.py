#!/usr/bin/env python3

import pkg_resources
import pytest

from aoc2021.d4 import Bingo, Board


@pytest.fixture
def bingo():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d4.txt")
    bingo: Bingo = Bingo.parse(filename)
    return bingo


def test_parse():
    filename = pkg_resources.resource_filename(__name__, "data/sample_d4.txt")
    bingo: Bingo = Bingo.parse(filename)
    assert len(bingo.draw) == 27
    assert len(bingo.boards) == 3
    assert bingo.boards[0].squaresize == 5


def test_turn5(bingo: Bingo):
    bingo.play(maxturn=5)
    marked: list[bool] = [False] * bingo.boards[0].size
    marked[0 * 5 + 3] = True  # 11
    marked[1 * 5 + 3] = True  # 4
    marked[2 * 5 + 1] = True  # 9
    marked[2 * 5 + 4] = True  # 7
    marked[3 * 5 + 4] = True  # 5
    b: Board = bingo.boards[0]
    assert b.marked == marked


def test_turn11(bingo: Bingo):
    bingo.play(maxturn=11)
    marked: list[bool] = [False] * bingo.boards[0].size
    marked[0 * 5 + 2] = True  # 17
    marked[0 * 5 + 3] = True  # 11
    marked[0 * 5 + 4] = True  # 0
    marked[1 * 5 + 1] = True  # 2
    marked[1 * 5 + 2] = True  # 23
    marked[1 * 5 + 3] = True  # 4
    marked[2 * 5 + 0] = True  # 21
    marked[2 * 5 + 1] = True  # 9
    marked[2 * 5 + 2] = True  # 14
    marked[2 * 5 + 4] = True  # 7
    marked[3 * 5 + 4] = True  # 5
    b: Board = bingo.boards[0]
    assert b.marked == marked


def test_game(bingo: Bingo):
    winner, number, turn = bingo.play()
    assert winner == bingo.boards[2]
    assert number == 24
    assert turn == 12
    expected = sum(winner.grid[i] for i, x in enumerate(winner.marked) if not x) * number
    assert expected == 4512


def test_lastwin(bingo: Bingo):
    bingo.keep_on_playing = True
    bingo.play()
    winner, number, turn = bingo.lastwin
    assert winner == bingo.boards[1]
    assert number == 13
    assert turn == 15  
    expected = sum(winner.grid[i] for i, x in enumerate(winner.marked) if not x) * number
    assert expected == 1924
    