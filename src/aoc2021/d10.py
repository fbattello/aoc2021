#!/usr/bin/env python3

from queue import LifoQueue
from aoc2021 import DATAPATH, SAMPLEPATH

OPENING = "([{<"
CLOSING = ")]}>"
PAIRMAPCLOSE = {")": "(", "]": "[", "}": "{", ">": "<"}
PAIRMAPOPEN = {"(": ")", "[": "]", "{": "}", "<": ">"}
SYNTAX_SCORE = {")": 3, "]": 57, "}": 1197, ">": 25137}
AUTOCOMPLETE_SCORE = {")": 1, "]": 2, "}": 3, ">": 4}


def parse(filename: str):
    with open(filename) as f:
        return f.read().splitlines()


def parseline(line: str) -> int:
    stack = LifoQueue()
    for token in line:
        if token in OPENING:
            stack.put(token)
        elif token in CLOSING:
            matchingtoken = stack.get()
            if PAIRMAPCLOSE[token] != matchingtoken:
                return SYNTAX_SCORE[token]
        else:
            return 0
    return 0


discard = lambda x: parseline(x) > 0


def autocomplete(line: str) -> str:
    completion = ""
    stack = LifoQueue()
    for token in line:
        if token in OPENING:
            stack.put(token)
        elif token in CLOSING:
            _ = stack.get()
    for _ in range(stack.qsize()):
        completion += PAIRMAPOPEN[stack.get()]
    return completion


def main():

    filename = DATAPATH.joinpath("input_d10.txt")
    # filename = SAMPLEPATH.joinpath("sample_d10.txt")
    lines = parse(filename)

    # part 1

    score = sum([parseline(l) for l in lines])
    print(score)

    # part 2

    lines = [x for x in lines if not discard(x)]
    completions = [autocomplete(line) for line in lines]
    scores: list[int] = []
    for completion in completions:
        score: int = 0
        for c in completion:
            score = score * 5 + AUTOCOMPLETE_SCORE[c]
        scores.append(score)
    scores.sort()
    middlescore = scores[len(scores) // 2]
    print(middlescore)


if __name__ == "__main__":
    main()
