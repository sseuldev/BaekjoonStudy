# 백준 25206 번. 너의 평점은

grade = 0.0
result = 0.0
score = {'A+' : '4.5', 'A0' : '4.0', 'B+' : '3.5', 'B0' : '3.0', 'C+' : '2.5', 'C0' : '2.0', 'D+' : '1.5', 'D0' : '1.0', 'F' : '0.0'}

for _ in range(20) :
    a, b, c = input().split()
    
    if c != 'P' :
        grade += float(b)
        result += float(b) * float(score[c])

print(round(result / grade, 6))