# 백준 10813 번. 공 바꾸기

N, M = map(int, input().split())
lst = []

for i in range(1, N + 1) :
    lst.append(i)

for m in range(M) :
    i, j = map(int, input().split())
    lst[i - 1], lst[j - 1] = lst[j - 1], lst[i - 1]

for i in lst :
    print(i, end = " ")


# 리스트 만들기 다르게 풀면,
# lst = [i for i in range(1, N + 1)] 도 가능!