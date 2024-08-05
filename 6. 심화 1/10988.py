# 백준 10988 번. 팰린드롬인지 확인하기

# 내 풀이
word = input()

print(1) if word == word[::-1] else print(0)


# 또 다른 풀이
word = input()
result = 1

for i in range(0, len(word) // 2) :
    if word[i] != word[len(word) - 1 - i] :
        result = 0

print(result)