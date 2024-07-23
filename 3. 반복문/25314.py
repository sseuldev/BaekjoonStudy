# 백준 25314 번. 코딩은 체육과목 입니다

# end 이용한 풀이
N = int(input())

for i in range(N // 4) :
    print('long ', end="")
print('int')


# 문자열 이용한 풀이
N = int(input())

answer = 'int'

for i in range(N // 4) :
    answer = 'long ' + answer

print(answer)


# 문자열 곱셈 이용한 풀이
N = int(input())

print(N // 4 * 'long ' + 'int')

