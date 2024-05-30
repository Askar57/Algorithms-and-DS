# Шейкерная сортировка сначала слева направо перемещая все большие элементы в конец, потом наоборот

def shaker_sort(array):
    length = len(array)
    swapped = True
    start_index = 0
    end_index = length - 1

    while (swapped == True):
        swapped = False

        # проход слева направо
        for i in range(start_index, end_index):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                print(arr)

        # если не было обменов прерываем цикл
        if (not (swapped)):
            break
        swapped = False
        end_index = end_index - 1

        # проход справа налево
        for i in range(end_index - 1, start_index - 1, -1):
            if (array[i] > array[i + 1]):
                # обмен элементов
                array[i], array[i + 1] = array[i + 1], array[i]
                swapped = True
                print(arr)
        start_index = start_index + 1


arr = [23, 2, 86, 345, 22, 1, 99, 12]
print(arr)
shaker_sort(arr)
