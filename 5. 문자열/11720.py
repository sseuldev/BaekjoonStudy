# 백준 11720 번. 숫자의 합

N = int(input())
num = input()
sum = 0

for i in range(N) :
    sum += int(num[i])

print(sum)


# 또 다른 풀이
N = int(input())
num = list(map(int, input()))

print(sum(num))