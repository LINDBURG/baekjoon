
inp = input().split()
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

profit = c-b
if profit > 0:
    print(a // profit + 1)
else:
    print(-1)
