# 백준 5622 번. 다이얼

# 내 풀이
letter = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
num = '22233344455566677778889999'

word = input()
time = len(word)

for i in word :
    time += int(num[letter.index(i)])

print(time)


# 리스트 이용한 풀이
dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
time = 0

for i in range(len(word)) :
    for j in dial :
        if word[i] in j :
            time += (dial.index(j) + 3)

print(time)


# 딕셔너리 이용한 풀이
dial = {'ABC' : 3, 'DEF' : 4, 'GHI' : 5, 'JKL' : 6, 'MNO' : 7, 'PQRS' : 8, 'TUV' : 9, 'WXYZ' : 10}
word = input()
time = 0

for i in word :
    for key, value in dial.items() :
        if i in key :
            time += value

print(time)
        
