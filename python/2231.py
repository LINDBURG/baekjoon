
n = int(input())

flag = 0
for i in range(0,n):
    tmp = i + sum(map(int,list(str(i))))
    if tmp == n:
        flag = 1
        print(i)
        break

if flag == 0:
    print(0)
