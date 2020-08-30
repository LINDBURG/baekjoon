import sys

class Time():
    def __init__(self, arr):
        self.N = len(arr)
        self.arr = arr
        self.max = 0
        self.run(0, 0)

    def run(self, idx, money):
        if idx >= self.N:
            if self.max < money:
                self.max = money
        else:
            self.run(idx+1,money)
            if self.arr[idx][0] + idx <= self.N:
                money += self.arr[idx][1]
            self.run(idx + self.arr[idx][0], money)

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int,sys.stdin.readline().split())))

time = Time(arr)
print(time.max)