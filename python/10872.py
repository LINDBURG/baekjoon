
n = int(input())

num = [1]
for i in range(1, n):
    num.append(num[i-1]*(i+1))
print(num[n-1])
