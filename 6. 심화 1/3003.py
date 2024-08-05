# 백준 3003 번. 킹, 퀸, 룩, 비숍, 나이트, 폰

lst = list(map(int, input().split()))
chess = [1, 1, 2, 2, 2, 8]

for i in range(6) :
    print(chess[i] - lst[i], end = ' ')