inp = input().split()
a = int(inp[0])
b = int(inp[1])
w = int(inp[2])
h = int(inp[3])

print(min(a, b, w-a, h-b))
