import sys
from itertools import combinations
from copy import deepcopy

class Castle():
    def __init__(self, n, m, d, board):
        self.allocations = list(combinations([i for i in range(m)], 3))
        self.board = board
        self.dist = d
        self.answer = 0
        for allocation in self.allocations:
            self.calc(allocation)

    def calc(self, allocation):
        count = 0
        board = deepcopy(self.board)
        m = len(board[0])
        for n in range(len(board),0,-1):
            remv = [[-30,-30],[-30,-30],[-30,-30]]
            for i in range(max(0,n-self.dist),n):
                for j in range(m):
                    if board[i][j] == 1:
                        for idx in range(3):
                            comp = allocation[idx]
                            dist = n-i + abs(comp-j)
                            n_dist = n-remv[idx][0] + abs(comp-remv[idx][1])
                            if dist <= self.dist and dist < n_dist:
                                remv[idx] = [i,j]
                            elif dist == n_dist and j <remv[idx][1]:
                                remv[idx] = [i,j]
            for i, j in remv:
                if i != -30 and board[i][j] == 1:
                    board[i][j] = 0
                    count += 1
            
            if count > self.answer:
                self.answer = count

N, M, D = map(int,sys.stdin.readline().split(' '))
board = []
for _ in range(N):
    board.append(list(map(int,sys.stdin.readline().split(' '))))

castle = Castle(N, M, D, board)
print(castle.answer)