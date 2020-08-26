import sys
from functools import reduce

class Paper():
    def __init__(self, board):
        self.board = board
        self.count = -1
        self.size = [0,0,0,0,0,0]
        self.depth = 0
        self.match()

    def match(self):
        write = 1
        if self.count != -1 and self.depth >= self.count:
            return 0
        for i in range(10):
            for j in range(10):
                if self.board[i][j] == 1:
                    write = 0
                    removable = self.check(i, j)
                    if removable:
                        for remove in removable:
                            self.remove(remove, i, j)
                            self.match()
                            self.restore(remove, i, j)
                    break
            if write == 0:
                break
        if write == 1:
            if self.count == -1 or self.depth < self.count:
                self.count = self.depth

    def check(self, row, col):
        available = []
        for size in range(1,6):
            if self.size[size] < 5 and  row + size < 11 and  col + size < 11:
                flag = 1
                for i in range(row, row+size):
                    for j in range(col, col+size):
                        if self.board[i][j] == 0:
                            flag = 0
                            break
                if flag == 1:
                    available.insert(0,size)
                else:
                    break
        return available

    def remove(self, size, k, l):
        for i in range(k, k+size):
            for j in range(l, l+size):
                self.board[i][j] = 0
        self.size[size] += 1
        self.depth += 1

    def restore(self, size, k, l):
        for i in range(k, k+size):
            for j in range(l, l+size):
                self.board[i][j] = 1
        self.size[size] -= 1
        self.depth -= 1

board = [list(map(int, sys.stdin.readline().split())) for _ in range(10)]
paper = Paper(board)
print(paper.count)