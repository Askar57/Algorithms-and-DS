# Cортировка прямым выбором
def selection(arr):
    n = len(arr)
    for i in range(n):
        min_i = i  # индекс текущего наименьшего элемента
        # Цикл проходит по оставшейся части массива
        for j in range(i + 1, n):
            # Если текущий элемент меньше, чем наименьший найденный до этого момента
            if arr[j] < arr[min_i]:
                min_i = j  # Обновляем индекс наименьшего элемента
        arr[i], arr[min_i] = arr[min_i], arr[i]
        print(arr)


arr = [23, 86, 2, 345, 22, 1, 99, 12]
print(arr)
selection(arr)
