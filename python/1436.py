import sys
n = int(sys.stdin.readline())

lst = ["666"]
while len(lst) < n + 5000:
    for i in range(len(lst)):
        for j in range(10):
            lst.append(str(j)+lst[i])
            lst.append(lst[i]+str(j))
    lst =list(set(lst))
lst = list(set(map(int,lst)))
lst.sort()
print(lst[n-1])

