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
    x = Solution()
    x.solvQueens(int(sys.argv[1]))


