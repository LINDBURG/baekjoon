
x = []
y = []
for i in range(3):
    inp = input().split()
    if inp[0] in x:
        x.remove(inp[0])
    else:
        x.append(inp[0])
    if inp[1] in y:
        y.remove(inp[1])
    else:
        y.append(inp[1])

print(x[0] + ' ' + y[0])

