
class HashTable:
    def __init__(self, size):
        self.size = size
        # Создание пустой таблицы заданного размера
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        # каждый ключ делится на размер таблицы (self.size)
        return key % self.size

    def put(self, key):
        index = self.hash_function(key)  # Вычисляем индекс для вставки
        # Вставляем ключ в соответствующую цепочку
        self.table[index].append(key)

    def display(self):
        for i in range(self.size):
            print(f"Ячейка {i}: {self.table[i]}")


# Пример использования
if __name__ == "__main__":
    keys = [5, 28, 19, 15, 20, 33, 12, 17, 10]
    table_size = 9
    hash_table = HashTable(table_size)

    # Вставляем ключи в хеш-таблицу
    for key in keys:
        hash_table.put(key)

    # Выводим содержимое хеш-таблицы
    hash_table.display()
