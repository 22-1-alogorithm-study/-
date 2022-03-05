# combination을 이용한 풀이(1)

from itertools import combinations  # 라이브러리 itertools에서 combination이란 수의 리스트에서 모든 조합을 나타내주는 명령어

while True:
    num_list = list(map(int, input().split()))
    k = num_list[0]

    if k == 0:
        break
    else:
        num = num_list[1:]

        for i in combinations(num, 6):
            for j in i:
                print(j, end=' ')
            print()
        print()
