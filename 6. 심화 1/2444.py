# 백준 2444 번. 별 찍기 - 7 

N = int(input())

for i in range(1, N) :
    print(' ' * (N - i) + '*' * (2 * i - 1))

for i in range(N, 0, -1) :
    print(' ' * (N - i) + '*' * (2 * i - 1))