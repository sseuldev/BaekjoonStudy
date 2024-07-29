# 백준 11718 번. 그대로 출력하기

# 방식 1 
while 1 :
    try :
        print(input())
    except :
        break


# 방식 2
import sys

print(sys.stdin.read())


# 방식 3
import sys

S = sys.stdin.readlines()

for i in S :
    print(i.rstrip())


# S = input().split('\n') 이 안되는 이유 바로잡기 !