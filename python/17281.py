from itertools import permutations
import sys

class Baseball():
    def __init__(self):
        self.max = 0
        self.entries = list(map(lambda x:list(x[:3]) + [0] + list(x[3:]), permutations([i for i in range(1,9)], 8)))
        self.innings = []
        self.memo = dict()

    def insert(self, line):
        line = list(map(int, line.split(' ')))
        self.innings.append(line)
        self.memo[len(self.memo)] = dict()

    def findmax(self):
        for entry in self.entries:
            score = 0
            idx = 0
            out = 0
            #print(entry)
            i = 0
            string = ''
            while i < len(self.innings):
                inning = self.innings[i]
                if inning[entry[idx]] > 0:
                    string += str(inning[entry[idx]])
                else:
                    out += 1
                idx = (idx + 1) % 9 
                if out == 3:
                    if string in self.memo[i]:
                        iscore = self.memo[i][string]
                    else:
                        iscore = self.calc(string)
                        self.memo[i][string] = iscore
                    score += iscore
                    string = ''
                    out = 0
                    i +=1 
                    continue
            if score > self.max:
                self.max = score
        return self.max

    def calc(self, hit):
        score = max(len(hit)-3, 0)
        tmp = 0
        for i in range(min(len(hit), 3)):
            if tmp + int(hit[-i-1]) > 3:
                score += 1
            tmp += int(hit[-i-1])
        return score


T = int(sys.stdin.readline())
baseball = Baseball()
for test_case in range(1, T + 1):
    baseball.insert(sys.stdin.readline())

print(baseball.findmax())
#print(baseball.memo)
