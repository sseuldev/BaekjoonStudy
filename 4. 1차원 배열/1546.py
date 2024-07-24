# 백준 1546 번. 평균

N = int(input())
lst = list(map(int, input().split()))
max_score = max(lst)

print(sum(lst) * 100 / max_score / N)