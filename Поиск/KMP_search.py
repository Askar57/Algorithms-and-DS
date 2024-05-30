def compute_prefix_function(pattern):
    # Функция для вычисления префикс-функции для строки-образца.
    m = len(pattern)
    prefix = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[j] == pattern[i]:
            prefix[i] = j + 1
            i += 1
            j += 1
            print(prefix)
        else:
            if j == 0:
                prefix[i] = 0
                i += 1
            else:
                j = prefix[j - 1]
    # Список значений префикс-функции для каждой позиции в строке-образце.
    return prefix


def knuth_morris_pratt(text, pattern):
    # Функция использует эту префикс-функцию для эффективного поиска образца в тексте.
    n = len(text)
    m = len(pattern)
    prefix = compute_prefix_function(pattern)

    i = 0  # Индекс для текста
    j = 0  # Индекс для образца

    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == m:
                return "Повтор найден"
        else:
            if j > 0:
                j = prefix[j - 1]
            else:
                i += 1

    return "Повтор не найден"


# Пример
text = "Cтрока найдена. Cтрока не найдена"
pattern = "не"
result = knuth_morris_pratt(text, pattern)
print(result)
