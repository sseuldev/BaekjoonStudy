# 백준 25304 번. 영수증

X = int(input())
N = int(input())

total = 0

for i in range(N) :
    a, b = map(int, input().split())
    total += a * b

if X == total :
    print('Yes')
else :
    print('No')
