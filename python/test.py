import sys
from itertools import combinations

class Lab():
    def __init__(self, N, M, walls):
        self.walls = walls
        self.empty_cnt = -3
        self.empty_max = 0
        self.empty = []
        self.poison = []
        for i in range(N):
            for j in range(M):
                if self.walls[i][j] == 0:
                    self.empty_cnt += 1
                    self.empty.append([i,j])
                elif self.walls[i][j] == 2:
                    self.poison.append([i,j])
        self.poison_min = self.empty_cnt
        
        for fst, scd, trd in combinations(self.empty, 3):
            self.run(fst, scd, trd)

    def run(self, fst, scd, trd):
        self.walls[fst[0]][fst[1]] = 1
        self.walls[scd[0]][scd[1]] = 1
        self.walls[trd[0]][trd[1]] = 1
        
        self.corrupted = 0
        self.queue = self.poison
        self.spread()

        self.walls[fst[0]][fst[1]] = 0
        self.walls[scd[0]][scd[1]] = 0
        self.walls[trd[0]][trd[1]] = 0

    def spread(self):
        if self.corrupted > self.poison_min:
            return 0
        while self.queue:



N,M = map(int,sys.stdin.readline().split())
walls = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
lab = Lab(N, M, walls)

#print(lab.comb)