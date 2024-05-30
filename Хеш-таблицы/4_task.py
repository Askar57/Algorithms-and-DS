
class HashTable:
    def __init__(self, size):
        self.size = size
        # Создание пустой таблицы заданного размера
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        A = (5 ** 0.5 - 1) / 2
        # Вычисление значения хеша
        hash_value = self.size * ((key * A) % 1)
        return int(hash_value)


# Пример использования
if __name__ == "__main__":
    keys = [61, 62, 63, 64, 65]
    table_size = 1000
    hash_table = HashTable(table_size)

    for key in keys:
        index = hash_table.hash_function(key)
        print(f"Ключ {key} хешируется в ячейку {index}")
