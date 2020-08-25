import sys
from functools import reduce
from copy import deepcopy

class Paper():
    def __init__(self, board):
        self.board = board
        self.count = -1
        self.left = [0,5,5,5,5,5]
        self.match(self.board, self.left, 0, 0)

    def match(self, board, left, i, j):
        ok = 1
        for i in range(i, 10):
            for j in range(j, 10):
                removable = self.check(board, i, j, left)
                if board[i][j] == 1 and not removable:
                    ok = 0
                    break
                for remove in removable:
                    nxt_board, nxt_left = self.remove(board, remove, left, i, j)
                    self.match(nxt_board, nxt_left, i, j)
            if ok == 0:
                break
        if ok == 1:
            print(left)
            print(board)
            if self.count == -1 or 25-sum(left) < self.count:
                self.count = 25 - sum(left)

    def check(self, board, row, col, left):
        available = []
        for size in range(1,6):
            if left[size] > 0 and  row + size < 11 and  col + size < 11:
                tmp = 1
                for i in range(row, row+size):
                    tmp *= reduce(lambda x, y: x*y, board[i][col:col+size])
                    if tmp == 0:
                        break
                if tmp == 1:
                    available.append(size)
                else:
                    break
        return available

    def remove(self, board, size, left, k, l):
        board = deepcopy(board)
        left = deepcopy(left)
        for i in range(k, k+size):
            for j in range(l, l+size):
                board[i][j] = 0
        left[size] -= 1
        return board, left
        

board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
paper = Paper(board)
print(paper.count)
print(paper.left)