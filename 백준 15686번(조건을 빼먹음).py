# 조건을 빼먹은 코드
import sys

def calc(x, y):
    res = abs(x[0]-y[0]) + abs(x[1]-y[1])
    return res

def length_road(x, y):
    total = []
    mid = []
    for i in x:
        for j in y:
            result = calc(i, j)
            mid.append(result)
        total.append(min(mid))
        mid.clear()
    res = sum(total)
    return res

input = sys.stdin.readline

N, M = map(int, input().split())
road_map = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
r = 0
c = 0
for i in range(N):
    r += 1
    c = 0
    for j in road_map[i]:
        c += 1
        if j == 1:
            home.append(list((r, c)))
        elif j == 2:
            chicken.append(list((r, c)))

print(length_road(home, chicken))

