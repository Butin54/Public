import random
def quicksort_random(array, left, right):    
    p = random.choice(array[left:right+1])
    i,j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1
        if j > left:
            quicksort_random(array, left, j)
    if right > i:
        quicksort_random(array, i, right)
    return array
def binary_search(array, element, left, right): 
    middle = (right+left) // 2
    if array[middle] >= element and array[middle-1] < element:
        return middle-1
    elif element < array[middle]:
        return binary_search(array, element, left, middle-1)
    else:
        return binary_search(array, element, middle+1, right)
array_number = []
while not array_number:
    try:
        array_number = list(map(int, input("Введите последовательность "\
                       "целых чисел через пробел").split()))
    except ValueError as e:
        print("Вы ввели последовательность чисел не корректно")
array_number = quicksort_random(array_number, 0, len(array_number)-1)
x = None
while not isinstance(x, int):
    try:
        x = int(input("Задайте целое число"))
    except ValueError as e:
        print("Ввод некорректен")
if x > array_number[-1]:
    print("В последовательности нет чисел, которые удовлетворяли бы условию отбора")
elif x <= array_number[0]:
    print("В последовательности нет чисел, которые удовлетворяли бы условию отбора")
else:
    print(array_number)
    print(x)
    print(binary_search(array_number, x, 0, len(array_number)-1))
