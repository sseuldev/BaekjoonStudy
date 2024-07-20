# 백준 2480 번. 주사위 세개

# 내 풀이
# a, b, c = map(int, input().split())

# if a == b == c :
#     print(10000 + a * 1000)
# elif a == b :
#     print(1000 + a * 100) 
# elif a == c :
#     print(1000 + a * 100) 
# elif b == c :
#     print(1000 + b * 100) 
# else :
#     print(max(a, b, c) * 100) 


# sorted 정렬을 이용한 풀이
a, b, c = map(int, input().split())

if a == b == c :
    print(10000 + a * 1000)
elif a == b or a == c or b == c :
    print(1000 + sorted([a, b, c])[1] * 100)
else :
    print(max(a, b, c) * 100) 