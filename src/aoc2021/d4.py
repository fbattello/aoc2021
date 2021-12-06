#!/usr/bin/env python3

from typing import Optional, TypeAlias
from dataclasses import dataclass
from math import sqrt
from aoc2021 import DATAPATH, SAMPLEPATH

Position: TypeAlias = tuple[int, int]


class Board:
    def __init__(self, numbers: list[int]):
        self.grid = numbers
        self.size = len(numbers)
        self.marked = [False] * self.size
        squaresize = sqrt(self.size)
        if not squaresize.is_integer():
            raise ValueError("Board must be square")
        self.squaresize = int(squaresize)
        self.rowmarkcounter: list[int] = [self.squaresize] * self.squaresize
        self.colmarkcounter: list[int] = [self.squaresize] * self.squaresize
        self.has_wined: bool = False

    def lookup(self, number: int) -> Position:
        ix = self.grid.index(number)
        icol = ix % self.squaresize
        irow = ix // self.squaresize
        return ix, irow, icol

    def reset(self):
        self.marked = [False] * self.size
        self.rowmarkcounter = [self.squaresize] * self.squaresize
        self.colmarkcounter = [self.squaresize] * self.squaresize


class Bingo:
    def __init__(
        self, draw: list[int], boards: list[Board], keep_on_playing: bool = False
    ):
        self.draw = draw
        self.boards = boards
        self.keep_on_playing: bool = keep_on_playing
        self.lastwin = None

    @classmethod
    def parse(cls, filename: str):
        with open(filename) as f:
            draw = [*map(int, next(f).rstrip().split(","))]
            boards: list[Board] = []
            b: str = ""
            for line in f:
                line = line.rstrip()
                if line == "":
                    if b:
                        board: Board = Board([*map(int, b.split())])
                        boards.append(board)
                    b = ""
                else:
                    b += line.rstrip() + " "
            print(f"{len(boards)} boards created")
            return cls(draw, boards)

    def play_turn(self, turn: int, n: int) -> Optional[Board]:
        winner: Board = None
        for b in self.boards:
            if b.has_wined:
                continue
            try:
                ix, irow, icol = b.lookup(n)
                b.marked[ix] = True
                b.rowmarkcounter[irow] -= 1
                b.colmarkcounter[icol] -= 1
                if b.rowmarkcounter[irow] == 0 or b.colmarkcounter[icol] == 0:
                    winner = b
                    self.lastwin = b, n, turn
                    winner.has_wined = True
                    if not self.keep_on_playing:
                        break
            except ValueError:
                pass
        return winner

    def play(self, *, maxturn: int = 0) -> tuple[Optional[Board], int, int]:
        draw = self.draw
        for turn, number in enumerate(draw, 1):
            winner = self.play_turn(turn, number)
            if (not self.keep_on_playing and winner) or turn == maxturn:
                return winner, number, turn
        return None, number, turn

    def reset(self):
        for board in self.boards:
            board.reset()


def main():
    filename = DATAPATH.joinpath("input_d4.txt")
    # filename = SAMPLEPATH.joinpath("sample_d4.txt")
    bingo = Bingo.parse(filename)

    print("Part 1")
    winner, number, turn = bingo.play()
    if winner:
        print(f"{winner=} {number=} {turn=}")
        total = sum(winner.grid[i] for i, x in enumerate(winner.marked) if not x)
        print(f"{total=}")
        print(total * number)
    else:
        print(f"{number=} {turn=}")

    print("-" * 32)
    print("Part 2")
    bingo.reset()
    bingo.keep_on_playing = True
    bingo.play()
    winner, number, turn = bingo.lastwin
    print(f"{winner=} {number=} {turn=}")
    total = sum(winner.grid[i] for i, x in enumerate(winner.marked) if not x)
    print(f"{total=}")
    print(total * number)


if __name__ == "__main__":
    main()
