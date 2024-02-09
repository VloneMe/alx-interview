#!/usr/bin/python3
"""
Solution to the N-queens problem
"""
import sys


def backtrack(r, n, cols, pos, neg, board):
    """
    Backtrack function to find solutions to the N-queens problem.

    Args:
        r (int): Current row.
        n (int): Number of queens.
        cols (set): Set of occupied columns.
        pos (set): Set of occupied positive diagonals.
        neg (set): Set of occupied negative diagonals.
        board (list): Current state of the chessboard.
    """
    if r == n:
        res = []
        for l in range(len(board)):
            for k in range(len(board[l])):
                if board[l][k] == 1:
                    res.append([l, k])
        print(res)
        return

    for c in range(n):
        if c in cols or (r + c) in pos or (r - c) in neg:
            continue

        cols.add(c)
        pos.add(r + c)
        neg.add(r - c)
        board[r][c] = 1

        backtrack(r+1, n, cols, pos, neg, board)

        cols.remove(c)
        pos.remove(r + c)
        neg.remove(r - c)
        board[r][c] = 0


def nqueens(n):
    """
    Solve the N-queens problem and print all solutions.

    Args:
        n (int): Number of queens. Must be at least 4.
    """
    cols = set()
    pos_diag = set()
    neg_diag = set()
    board = [[0] * n for _ in range(n)]

    backtrack(0, n, cols, pos_diag, neg_diag, board)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        nn = int(sys.argv[1])
        if nn < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(nn)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
