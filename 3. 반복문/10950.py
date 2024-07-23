# 백준 10950 번. A + B - 3

# 내 풀이
T = int(input())

for i in range(T) :
    a, b = map(int, input().split())
    print(a + b)



# 또 다른 풀이 (리스트와 sum 함수 이용)
T = int(input())

for i in range(T) :
    lst = list(map(int, input().split()))
    print(sum(lst))
