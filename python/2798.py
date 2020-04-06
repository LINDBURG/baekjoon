from itertools import combinations

inp = input().split()
M = int(inp[1])

inp = input().split()
lst = list(map(int, inp))

com = list(set(map(sum, combinations(lst,3))))
com.sort()
for i in range(len(com)-1,-1,-1):
    if com[i] <= M:
        print(com[i])
        break

