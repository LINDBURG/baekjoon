import sys

class Pipe():
    def __init__(self, n, house):
        self.count = [[[0, 0, 0] for _ in range(n)] for _ in range(n)]
        self.count[0][1][0] = 1
        self.house = house
        self.run()


    def run(self):
        house = self.house
        count = self.count
        for i in range(len(self.count)):
            for j in range(2, len(self.count)):
                if house[i][j] == 0:
                    #가로
                    count[i][j][0] = count[i][j-1][0] + count[i][j-1][1]
                    #세로
                    count[i][j][2] = count[i-1][j][1] + count[i-1][j][2]
                #대각선
                if i*j != 0 and house[i][j] == 0 and house[i-1][j] == 0 and house[i][j-1] == 0:
                    count[i][j][1] = count[i-1][j-1][0] + count[i-1][j-1][1] + count[i-1][j-1][2]
        self.solution = sum(count[-1][-1])



n = int(sys.stdin.readline())

house = []
for _ in range(n):
    tmp = list(map(int, sys.stdin.readline().split(' ')))
    house.append(tmp)

pipe = Pipe(n, house)

print(pipe.solution)