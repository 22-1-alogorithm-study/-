import sys

input = sys.stdin.readline

x = int(input())

stick = []

s_len = 64
total = 0

while total != x:
    if x == s_len:
        stick.append(s_len)
        break
    else:
        s_len = s_len // 2
        stick.append(s_len)
        total = sum(stick)
        if total > x:
            stick.remove(s_len)

print(len(stick))


