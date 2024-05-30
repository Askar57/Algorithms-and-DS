def linear_search(array, n, value):
    for i in range(0, n):
        if (array[i] == value):
            return i
    return -1


array = [1, 3, 5, 11, 100, 121]
value = 3
n = len(array)

res = linear_search(array, n, value)
if (res == -1):
    print("Не найден")
else:
    print("Элемент", value, "найден по индексу:", res)
