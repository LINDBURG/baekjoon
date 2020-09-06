import sys
from math import ceil

class Room():
    def __init__(self, student, senior, junior):
        self.student = student
        self.senior = senior
        self.junior = junior
        self.cnt = len(student)
        self.calc()

    def calc(self):
        for num in self.student:
            num -= self.senior
            if num > 0:
                self.cnt += ceil(num / self.junior)



N = int(sys.stdin.readline())
student = list(map(int,sys.stdin.readline().split()))
senior, junior = map(int, sys.stdin.readline().split())
room = Room(student, senior, junior)

print(room.cnt)