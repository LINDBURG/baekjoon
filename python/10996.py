N = int(input())

for i in range(2*N):
    if i % 2 ==0:
        s = "*"
        for j in range((N-1)//2):
            s += " *"
        print(s)
    elif N != 1:
        s = ""
        for j in range(N//2):
            s += " *"
        print(s)

