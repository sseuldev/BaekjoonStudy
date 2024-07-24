# 백준 10818 번. 최소, 최대

# 메서드 이용한 방법
N = int(input())
lst = list(map(int, input().split()))

print(min(lst), max(lst))


# 직접 최대, 최소 구하는 방법
N = int(input())
lst = list(map(int, input().split()))
min = lst[0]
max = lst[0]

for i in lst[1:] :
    if min > i :
        min = i
    if max < i :
        max = i

print(min, max)