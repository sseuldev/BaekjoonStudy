# 백준 8393 번. 합

# 반복문 이용한 풀이
n = int(input())
answer = 0

for i in range(1, n+1) :
    answer += i

print(answer)

# 수학 공식 이용한 풀이
n = int(input())

print(int(n * (n + 1) / 2))