# 백준 5597 번. 과제 안 내신 분..?

lst = [i for i in range(1, 31)]

for i in range(28) :
    n = int(input())
    lst.remove(n)

print(lst[0])
print(lst[1])

# print(*lst, sep = "\n") 도 가능!