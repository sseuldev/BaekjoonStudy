# 백준 1157 번. 단어 공부

# 내 풀이
word = input().upper()
word_set = list(set(word))
lst = [0] * len(word_set)

for i in range(0, len(word_set)) :
    lst[i] = word.count(word_set[i])

if lst.count(max(lst)) == 1 :
    i = word_set[lst.index(max(lst))]
    print(word[word.index(i)])
else :
    print('?')


# 좀 더 깔끔한 풀이
word = input().upper()
word_list = list(set(word))
lst = []

for i in word_list :
    lst.append(word.count(i))

if lst.count(max(lst)) > 1 :
    print('?')
else :
    print(word_list[lst.index(max(lst))])




