# 백준 2439 번. 별 찍기 - 2

N = int(input())

for i in range(1, N + 1) :
    print(' ' * (N - i) + '*' * i)