from random import randint

inteiros = [randint(1, 100) for i in range(15)]


def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp


bubbleSort(inteiros)
print(inteiros)