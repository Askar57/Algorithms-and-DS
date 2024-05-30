# Cортировка прямым обменом (пузырьковая)

def bubble(arr):
    n = len(arr)
    for i in range(n):
        # Внутренний цикл
        for j in range(0, n-i-1):
            # Если текущий элемент больше следующего, то они должны поменяться местами
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)


arr = [23, 86, 2, 345, 22, 100, 1, 99]
print(arr)
bubble(arr)
