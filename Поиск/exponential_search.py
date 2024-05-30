# Экспоненциальный поиск

def exponential_search(arr, value):
    n = len(arr)

    # Если целью является первый элемент, вернуть его индекс
    if arr[0] == value:
        return 0

    # Находиться диапазон для бинарного поиска путем многократного удвоения
    i = 1
    while i < n and arr[i] <= value:
        i *= 2

    # Выполняется двоичный поиск
    return binary_search(arr, value, i // 2, min(i, n - 1))


def binary_search(arr, value, left, right):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == value:
            return mid
        elif arr[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return -1


arr = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
value = 16
result = exponential_search(arr, value)
if result != -1:
    print("Элемент", value, "найден по индексу:", result)
else:
    print("Элемент не найден")
