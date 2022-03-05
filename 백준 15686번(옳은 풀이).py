import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
road_map = [list(map(int, input().split())) for _ in range(N)]

home = []
chicken = []
result = []
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
            
pos_c = list(combinations(chicken, M))

def calc(home, chicken):
    min_distance = 1e9  # 최초 최소 거리값

    for c in chicken:
        dist = abs(c[0] - home[0]) + abs(c[1] - home[1])
        min_distance = min(min_distance,  dist)

    return min_distance

for i in pos_c:
    total = 0
    for j in home:
        total += calc(j, i)
    result.append(total)

print(min(result))

