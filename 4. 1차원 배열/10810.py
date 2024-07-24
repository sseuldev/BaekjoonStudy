# 백준 10810 번. 공 넣기

# 내 풀이
N, M = map(int, input().split())
lst = []

for i in range(N) :
    lst.append(0)

for m in range(M) :
    i, j, k = map(int, input().split())

    for n in range(i - 1, j) :
        lst[n] = k

for i in lst :
    print(i, end = " ")


# 리스트의 원소를 다 0으로 채울 경우
# 반복문이 아닌 간단히 곱셈을 이용하면 된다!
# lst = [0] * N
