# dsf 를 이용한 풀이

import sys
input = sys.stdin.readline

def dfs(s, depth):
    if depth == 6:
        print(' '.join(map(str, comb_n)))
        return

    for i in range(s, len(num)):
        comb_n[depth] = num[i]
        dfs(i+1, depth+1)  # 1씩 증가시켜 재귀(시간은 오래걸릴 수 있음)


while True:
    num_list = list(map(int, input().split()))
    k = num_list[0]
    num = num_list[1:]
    
    if k == 0:
        break

    comb_n = [0] * 6
    dfs(0, 0)
    print()
        
