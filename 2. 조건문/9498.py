# 백준 9498 번. 시험 성적

# 내 풀이
score = int(input())

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else :
    print('F')


# 더 나은 풀이
score = int(input())
grade = 'FFFFFFDCBAA'

print(grade[score // 10])