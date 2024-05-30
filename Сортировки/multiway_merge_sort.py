# многопутевая сортировка
def multiway_merge_sort(arr, k):
    if len(arr) <= 1:
        return arr
    # Разбиваем массив на k частей
    partitions = [[] for _ in range(k)]
    for i, item in enumerate(arr):
        partitions[i % k].append(item)

    # Рекурсивно вызываем функцию multiway_merge_sort для каждой части и получаем отсортированные подмассивы
    sorted_partitions = [multiway_merge_sort(part, k) for part in partitions]

    # Сливаем отсортированные подмассивы с помощью функции k_way_merge
    result = k_way_merge(sorted_partitions)
    return result


def k_way_merge(sorted_lists):
    # Список для хранения текущего элемента каждого отсортированного подсписка
    current_items = [0] * len(sorted_lists)
    result = []

    # Цикл продолжается, пока все подсписки не будут обработаны
    while any(current_items[i] < len(sorted_lists[i]) for i in range(len(sorted_lists))):

        # Ищем минимальный элемент среди текущих элементов каждого подсписка
        min_item = float('inf')
        min_index = -1
        for i, lst in enumerate(sorted_lists):
            if current_items[i] < len(lst) and lst[current_items[i]] < min_item:
                min_item = lst[current_items[i]]
                min_index = i

        # Добавляем минимальный элемент в результирующий массив и обновляем указатель текущего элемента для соответствующего списка
        result.append(min_item)
        current_items[min_index] += 1

    return result


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    with open(input_file, 'r') as f:
        s = f.read()
        s1 = s.split()
        arr = [int(i) for i in s1]

    arr = multiway_merge_sort(arr, 5)
    # arr - массив для сортировки.
    # k - количество частей, на которые будет разбит массив.

    with open(output_file, 'w') as f:
        for i in arr:
            f.write(str(i) + ' ')
