#!/usr/bin/python3
"""Defining nQuineens class."""


class Solution:
    """Returns array of arrays or nquines."""

    def solvQueens(self, n: int):
        col = []
        posDiag = []
        negDiag = []

        bd = []

        def backtrack(r):
            """Backtrack function."""

            nonlocal bd, col, posDiag, negDiag
            if r == n:
                print(bd)
                return

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.append(c)
                posDiag.append(r+c)
                negDiag.append(r-c)
                bd.append([r, c])

                backtrack(r+1)

                col.pop()
                posDiag.pop()
                negDiag.pop()
                bd.pop()

        backtrack(0)
        return


if __name__ == '__main__':
    import sys
    s = sys.argv[1]
    isInt = True
    try:
        s = int(s)
    except ValueError:
        isInt = False
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not isInt:
        print("N must be a number")
        exit(1)
    if s < 4:
        print("N must be at least 4")
        exit(1)
    x = Solution()
    x.solvQueens(s)
