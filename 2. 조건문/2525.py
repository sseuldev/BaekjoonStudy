# 백준 2525 번. 오븐 시계

# 평범한 풀이
# hour, min = map(int, input().split())
# time = int(input())

# cal_hour = (min + time) // 60
# cal_min = (min + time) % 60

# if hour + cal_hour > 23 :
#     print(hour + cal_hour - 24, cal_min)
# else :
#     print(hour + cal_hour, cal_min)



# 나머지 연산 활용해 본 풀이 
hour, min = map(int, input().split())
time = int(input())

total = hour * 60 + min + time

print((total // 60) % 24, total % 60)
