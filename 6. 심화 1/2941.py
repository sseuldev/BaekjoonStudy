# 백준 2941 번. 크로아티아 알파벳

# 내 풀이
word = input()
count = 0
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst :
    if i in word :
        count = count + word.count(i)

print(len(word) - count)


# 또 다른 풀이
word = input()
lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in lst :
    word = word.replace(i, '*')

print(len(word))