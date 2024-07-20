# 백준 2884 번. 알람 시계

hour, min = map(int, input().split())

cal = min - 45

if cal >= 0 :
    print(hour, cal)
else :
    if hour == 0 :
        print(23, 60 + cal)
    else :
        print(hour - 1, 60 + cal)