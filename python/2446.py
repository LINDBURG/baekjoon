N = int(input())

for i in range(N):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (N - i) - 1):
        print("*", end="")
    print("\n", end="")


for i in range(N-2, -1, -1):
    for j in range(i):
        print(" ", end="")
    for j in range(2 * (N - i) - 1):
        print("*", end="")
    print("\n", end="")

