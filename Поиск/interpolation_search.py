# Интерполяционный поиск

def interpolation_search(arr, key):
    left = 0  # Левая граница поиска
    right = len(arr) - 1  # Правая граница поиска

    while left <= right and arr[left] <= key <= arr[right]:
        # Интерполируем позицию mid для сравнения
        mid = left + ((key - arr[left]) * (right - left)
                      ) // (arr[right] - arr[left])

        if arr[mid] < key:
            left = mid + 1
        elif arr[mid] > key:
            right = mid - 1
        else:
            return mid

    if arr[left] == key:
        return left
    elif arr[right] == key:
        return right
    else:
        return -1  # Если такого элемента в массиве нет


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
key = 16
result = interpolation_search(arr, key)
if result != -1:
    print("Элемент", key, "найден по индексу:", result)
else:
    print("Элемент не найден")
