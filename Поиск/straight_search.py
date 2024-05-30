def straight_search(full_str, in_str):
    full_len = len(full_str)
    print(full_len)
    in_len = len(in_str)
    print(in_len)
    for i in range(full_len - in_len + 1):
        count = 0
        # Если все символы совпадают, он увеличивает счетчик count на 1.
        while count < in_len and full_str[i + count] == in_str[count]:
            count += 1
        # Если все символы в in_str совпадают с символами в full_str,
        # то он возвращает индекс начала совпадения
        if count == in_len:
            return i
    return -1


full_str = "Cтрока найдена. Cтрока не найдена"
in_str = "не"

res = straight_search(full_str, in_str)

if res == -1:
    print("Cтрока не найдена")
else:
    print("Cтрока найдена. Её индекс начинается с", res)
