import sys

input = sys.stdin.readline

N, L = map(int, input().split())

for i in range(L, 101): # 100 이하여야한다.
    num = N - (i * (i + 1) / 2)

    if num % i == 0:   # 정수일 경우에만 해당
        num = int(num / i)

        if num >= -1:  #양의 정수일 때만 해당
            for j in range(1, i + 1):
                print(num + j, end=' ')
            break
else:
    print(-1)
