# 백준 10811 번. 바구니 뒤집기

N, M = map(int, input().split())
lst = [i for i in range(1, N + 1)]

for _ in range(M) :
   i, j = map(int, input().split())
   temp = lst[i - 1 : j]
   temp.reverse()
   lst[i - 1 : j] = temp

print(*lst)