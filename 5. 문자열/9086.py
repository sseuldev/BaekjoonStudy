# 백준 9086 번. 문자열

T = int(input())

for _ in range(T) :
    S = input()
    print(S[0] + S[len(S) - 1])


# 마지막 문자는 간단하게 S[-1]로 표현 가능!
# S[-1]