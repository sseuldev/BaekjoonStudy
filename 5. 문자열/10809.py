# 백준 10809 번. 알파벳 찾기

# for문 이용한 방식
S = list(input())
word = 'abcdefghijklmnopqrstuvwxyz'

for i in word :
    if i in S :
        print(S.index(i), end=' ')
    
    else :
        print(-1, end=' ')


# find 함수 이용한 방식
S = input()
word = 'abcdefghijklmnopqrstuvwxyz'

for i in word :
    print(S.find(i))
    













