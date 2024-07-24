# 백준 10871 번. X보다 작은 수

N, X = map(int, input().split())
lst = list(map(int, input().split()))

for i in lst :
    if i < X :
        print(i, end=" ")
