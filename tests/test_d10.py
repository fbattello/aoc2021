#!/usr/bin/env python3

from aoc2021.d10 import *

lines = [
    r"[({(<(())[]>[[{[]{<()<>>",  # 0
    r"[(()[<>])]({[<{<<[]>>(",  # 1
    r"{([(<{}[<>[]}>{[]{[(<()>",  # 2 - corrupted
    r"(((({<>}<{<{<>}{[]{[]{}",  # 3
    r"[[<[([]))<([[{}[[()]]]",  # 4 - corrupted
    r"[{[{({}]{}}([{[{{{}}([]",  # 5 - corrupted
    r"{<[[]]>}<{[{[{[]{()[[[]",  # 6
    r"[<(<(<(<{}))><([]([]()",  # 7 - corrupted
    r"<{([([[(<>()){}]>(<<{{",  # 8 - corrupted
    r"<{([{{}}[<[[[<>{}]]]>[]]",  # 9
]

corrupted = [
    r"{([(<{}[<>[]}>{[]{[(<()>",
    r"[[<[([]))<([[{}[[()]]]",
    r"[{[{({}]{}}([{[{{{}}([]",
    r"[<(<(<(<{}))><([]([]()",
    r"<{([([[(<>()){}]>(<<{{",
]

incomplete = [  # [l for l in lines if l not in corrupted]
    r"[({(<(())[]>[[{[]{<()<>>",
    r"[(()[<>])]({[<{<<[]>>(",
    r"(((({<>}<{<{<>}{[]{[]{}",
    r"{<[[]]>}<{[{[{[]{()[[[]",
    r"<{([{{}}[<[[[<>{}]]]>[]]",
]


def test_basic():
    assert len(lines) == 10
    assert len(corrupted) == 5
    assert len(incomplete) == 5


def test_parser():
    scores = [parseline(l) for l in lines]
    assert scores == [0, 0, 1197, 0, 3, 57, 0, 3, 25137, 0]


def test_autocomplete_line_4():
    line = r"<{([{{}}[<[[[<>{}]]]>[]]"
    assert autocomplete(line) == "])}>"


def test_autocomplete_line_3():
    line = r"{<[[]]>}<{[{[{[]{()[[[]"
    assert autocomplete(line) == "]]}}]}]}>"


def test_autocomplete_line_2():
    line = r"(((({<>}<{<{<>}{[]{[]{}"
    assert autocomplete(line) == "}}>}>))))"


def test_autocomplete_line_1():
    line = r"[(()[<>])]({[<{<<[]>>("
    assert autocomplete(line) == ")}>]})"


def test_autocomplete_line_0():
    line = r"[({(<(())[]>[[{[]{<()<>>"
    assert autocomplete(line) == "}}]])})]"
