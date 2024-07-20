# 백준 2588번. 곱셈

A = int(input())
B = input()

print(A * int(B[2]))
print(A * int(B[1]))
print(A * int(B[0]))

print(A * int(B))

# 반복문 사용하는 방법도 존재
# for i in range(3, 0, -1) :
#     print(A * int(B[i - 1]))