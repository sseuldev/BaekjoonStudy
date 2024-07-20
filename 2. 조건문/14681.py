# 백준 14681 번. 사분면 고르기

# 내 풀이
num_x = int(input())
num_y = int(input())

if num_x > 0 :
    if num_y > 0 :
        print('1')
    else :
        print('4')
else :
    if num_y > 0 :
        print('2')
    else :
        print('3')



# 이진 논리를 이용한 다른 풀이
# 양수: 1 음수 : 0 으로 하고 최종값을 이진값으로 바꿔보자
# 1사분면 (1, 1) : 3 & 2사분면 (0, 1) : 1 & 3사분면 (0, 0) : 0 & 4사분면 (1, 0) : 2
# 이진수 : 0-1-2-3 -> 사분면 : 3-2-4-1 순

num_x = int(input())
num_y = int(input())

quads = [3, 2, 4, 1]

# true면 1, false면 0 
x_y_2 = (num_x > 0, num_y > 0)

x_y_10 = x_y_2[0] * 2 + x_y_2[1]

print(quads[x_y_10])
