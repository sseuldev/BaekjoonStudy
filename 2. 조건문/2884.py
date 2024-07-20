# 백준 2884 번. 알람 시계

# 내 풀이
hour, min = map(int, input().split())

cal = min - 45

if cal >= 0 :
    print(hour, cal)
else :
    if hour == 0 :
        print(23, 60 + cal)
    else :
        print(hour - 1, 60 + cal)


# 분 단위로 바꾼 뒤 나머지 연산 활용하는 풀이
hour, min = map(int, input().split())

total = hour * 60 + min

# total이 음수인 경우를 대비하기 위해 1440(24 * 60)으로 나머지 연산 해준 것 !
answer = (total - 45) % 1440        
print(answer // 60, answer % 60)