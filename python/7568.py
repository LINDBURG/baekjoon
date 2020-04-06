
n = int(input())

size = []
ans = ""
for i in range(n):
    tmp = list(map(int, input().split()))
    size.append(tmp)

for a,b in size:
    cnt = 1
    for c,d in size:
        if a<c and b<d:
            cnt += 1
    ans += str(cnt) + " "
print(ans[:-1])
