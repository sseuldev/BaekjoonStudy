# 백준 3052 번. 나머지

# 내 풀이 : 리스트에 not in 기능 이용
lst = []

for i in range(10) :
    n = int(input())

    if n % 42 not in lst :
        lst.append(n % 42)

print(len(lst))


# 다른 풀이 : set 집합 자료형 이용
# 중복 제거 위함
num = set()

for i in range(10) :
    n = int(input())
    num.add(n % 42)

print(len(num))