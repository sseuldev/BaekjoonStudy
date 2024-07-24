# 백준 2562 번. 최댓값
lst = []

for i in range(9) :
    N = int(input())
    lst.append(N)

print(max(lst))
print(lst.index(max(lst))+ 1)