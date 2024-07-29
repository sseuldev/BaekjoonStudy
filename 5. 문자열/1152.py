# 백준 1152 번. 단어의 개수

# 내 풀이
S = input()

if S[0] == ' ' and S[-1] == ' ' :
    print(S.count(' ') - 1)
elif S[0] == ' ' or S[-1] == ' ' :
    print(S.count(' '))
else :
    print(S.count(' ') + 1)


# 더 나은 풀이
S = input().split()
print(len(S))