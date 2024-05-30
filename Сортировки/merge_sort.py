# Сортировка прямым слиянием
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Рекурсивно сортируем обе половины
        merge_sort(left_half)
        merge_sort(right_half)

        # Слияние отсортированных половин
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Проверяем, остались ли элементы в левой и правой половинах
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1


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
    merge_sort(data)
    write_data_to_file(output_file, data)
