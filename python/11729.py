
def hanoi(num, start, end):
    mid = 6 - start - end

    if num == 1:
        print(start, end)
    else:
        hanoi(num-1, start, mid)
        print(start, end)
        hanoi(num-1, mid, end)

n = int(input())

cnt = 0
for i in range(n):
    cnt = cnt*2 + 1
print(cnt)

hanoi(n, 1, 3)
