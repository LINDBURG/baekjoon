
n = int(input())

num = [0,1]
for i in range(1, n):
    num.append(num[-1] + num[-2])
print(num[n])
