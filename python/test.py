import sys
n = int(sys.stdin.readline())
lst = []
cnt = {}

for i in range(n):
    num = int(sys.stdin.readline())
    lst.append(num)
    if num in cnt:
        cnt[num] += 1
    else:
        cnt[num] = 1
    
lst.sort()
cnt = sorted(cnt.items(), key = lambda x: (-x[1], x[0]))

print(round(sum(lst)/n))
print(lst[n//2])

if len(cnt) == 1:
    print(cnt[0][0])
elif cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
    
print(lst[-1] - lst[0])
