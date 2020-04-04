def nstar(cnt, inp):

    n = []
    for s in inp:
        n.append(s*3)
    for s in inp:
        n.append(s + " "*len(s) + s)
    for s in inp:
        n.append(s*3)
        
    return n


n = int(input())

cnt =0
for i in range(n):
    if 3**i == n:
        cnt = i
        break

inp = ["*"]
for i in range(cnt):
    inp = nstar(cnt, inp)
for i in range(len(inp)):
    print(inp[i])
