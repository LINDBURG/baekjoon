
while True:
    inp = input().split()
    inp = list(map(int, inp))
    if not any(inp):
        break
    mx = max(inp)
    inp.remove(mx)
    if mx**2 == inp[0]**2 + inp[1]**2:
        print("right")
    else:
        print("wrong")

