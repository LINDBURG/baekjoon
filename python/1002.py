
n = int(input())
for i in range(n):
    inp = list(map(int, input().split()))
    dist = ((inp[0] - inp[3])**2 + (inp[1] - inp[4])**2) ** (1/2)
    
    if inp[0] == inp[3] and inp[1] == inp[4] and inp[2] == inp[5]:
        print(-1)
    elif abs(dist - inp[2] - inp[5]) < 0.0001 or abs(dist - abs(inp[2] - inp[5])) < 0.0001:
        print(1)
    elif dist > inp[2] + inp[5] or dist < abs(inp[2] - inp[5]):
        print(0)
    else:
        print(2)
