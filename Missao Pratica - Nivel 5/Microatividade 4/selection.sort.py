from random import randint

inteiros = [randint(1, 100) for i in range(15)]

print(inteiros)
for i in range(len(inteiros)):
    temp = i
    for j in range(i + 1, len(inteiros)):
        if inteiros[temp] > inteiros[j]:
            temp = j
    inteiros[i], inteiros[temp] = inteiros[temp], inteiros[i]


print(inteiros)
