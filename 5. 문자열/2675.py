# 백준 2675 번. 문자열 반복

for _ in range(int(input())) :
    R, S = input().split()

    for i in S :
        print(i * int(R), end='')

    print()