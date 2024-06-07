import sys
input = sys.stdin.readline

N = int(input())
lines = []

for _ in range(N):
    lines.append(tuple(map(int, input().split())))

lines.sort()

left = lines[0][0]
right = lines[0][1]
ans = 0

for i in range(1, N):
    if right >= lines[i][1]:
        continue
    
    elif lines[i][0] <= right < lines[i][1]:
        right = lines[i][1]
    
    elif right < lines[i][0]:
        ans += right - left
        left = lines[i][0]
        right = lines[i][1]

ans += right - left
print(ans)