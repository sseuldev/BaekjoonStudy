# 백준 2908 번. 상수

# 내 풀이
a, b = input().split()

if int(a[-1]+a[-2]+a[-3]) > int(b[-1]+b[-2]+b[-3]) :
    print(a[-1]+a[-2]+a[-3])
else :
    print(b[-1]+b[-2]+b[-3])


# 더 나은 풀이
a, b = input().split()

a = int(a[::-1])
b = int(b[::-1])

print(a) if a > b else print(b)