
inp = input().split()
a = int(inp[0])
b = int(inp[1])
v = int(inp[2])

ans = (v-b) / (a-b)
if ans - int(ans) > 0:
    ans += 1
print(int(ans))



#3 2 5
#3 1 5
