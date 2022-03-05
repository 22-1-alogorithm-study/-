import sys

input = sys.stdin.readline

N = int(input())
rope = []
result = []

for _ in range(N):
    rope.append(int(input()))
rope.sort()

for i in rope:
    res = i * N
    result.append(res)
    N -= 1
    
print(max(result))
