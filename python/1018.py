inp = input().split()
n = int(inp[0])
m = int(inp[1])
board = []
mini = 64

for i in range(n):
    board.append(list(input()))
    
for i in range(n-7):
    for j in range(m-7):
        B = 0
        for r in range(i,i+8):
            for c in range(j,j+8):
                if (board[r][c] == "B" and (r+c)%2 == 0) or (board[r][c] == "W" and (r+c)%2==1):
                    B += 1
        cnt = min(64-B, B)
        if cnt < mini:
            mini = cnt

print(mini)
