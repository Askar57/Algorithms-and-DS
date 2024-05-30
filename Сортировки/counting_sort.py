# Сортировка подсчетом
def counting_sort(arr):
    # Определение максимального значения в массиве
    max_val = max(arr)

    # Создание массива для подсчета встречаемости каждого элемента
    count = [0] * (max_val + 1)

    # Подсчет
    for num in arr:
        count[num] += 1

    # Формирование отсортированного списка
    sorted_arr = []
    for i in range(len(count)):
        sorted_arr.extend([i] * count[i])

    return sorted_arr


if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Исходный массив:", arr)

    sorted_arr = counting_sort(arr)

    print("Отсортированный массив:", sorted_arr)
