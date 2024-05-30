# Алгоритм естественного слияния.
def natural_merge_sort(arr):
    # Функция для слияния двух подмассивов в один отсортированный массив
    def merge(arr, left, mid, right):
        left_subarray = arr[left:mid + 1]  # левый подмассив
        right_subarray = arr[mid + 1:right + 1]  # правый подмассив

        i = j = 0
        k = left

        # Слияние подмассивов
        while i < len(left_subarray) and j < len(right_subarray):
            if left_subarray[i] <= right_subarray[j]:
                arr[k] = left_subarray[i]
                i += 1
            else:
                arr[k] = right_subarray[j]
                j += 1
            k += 1

        # Копирование оставшихся элементов из левого подмассива
        while i < len(left_subarray):
            arr[k] = left_subarray[i]
            i += 1
            k += 1

        # Копирование оставшихся элементов из правого подмассива
        while j < len(right_subarray):
            arr[k] = right_subarray[j]
            j += 1
            k += 1

    n = len(arr)
    size = 1

    # Начинаем сортировку с подмассивов размером 1 и увеличиваем размер в два раза на каждой итерации
    while size < n - 1:
        left = 0
        # Обрабатываем пары подмассивов и сливаем их в один отсортированный массив
        while left < n - 1:
            mid = min(left + size - 1, n - 1)  # середина первого подмассива
            right = min(left + 2 * size - 1, n - 1)  # конец второго подмассива
            merge(arr, left, mid, right)  # слияние подмассивов
            left += 2 * size  # переходим к следующей паре подмассивов
        size *= 2  # увеличиваем размер подмассива вдвое


def read_data_from_file(input_file):
    with open(input_file, 'r') as f:
        data = [int(line.strip()) for line in f]
    return data


def write_data_to_file(output_file, data):
    with open(output_file, 'w') as f:
        for item in data:
            f.write("%s\n" % item)


if __name__ == "__main__":
    input_file = "input.txt"
    output_file = "output.txt"

    data = read_data_from_file(input_file)
    natural_merge_sort(data)
    write_data_to_file(output_file, data)
