def binary_search(array, value, left, right, center):

    while array[center] != value:
        print(array[center])
        print(left)
        print(right)
        print('------')
        if value > array[center]:
            left = center + 1
        else:
            right = center - 1
        center = (left + right) // 2
        if left >= right:
            break

    if value == array[center]:
        print("Элемент", value, "найден по индексу:", center)

    else:
        print("Не найден")


array = [1, 3, 5, 11, 100, 121]
value = 11

left = 0
right = len(array) - 1
center = (left + right) // 2

binary_search(array, value, left, right, center)
