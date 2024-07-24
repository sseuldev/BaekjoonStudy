# 백준 10807 번. 개수 세기

# 내장 메소드 쓰는 방법
N = int(input())
lst = list(map(int, input().split()))
v = int(input())

print(lst.count(v))


# 내장 메소드 없이 풀기
N = int(input())
lst = list(map(int, input().split()))
v = int(input())
count = 0

for i in lst :
    if i == v :
        count += 1

print(count)