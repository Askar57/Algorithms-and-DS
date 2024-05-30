class DirectAddressTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size  # Инициализируем массив заданного размера

    def insert(self, key, value):
        index = self.hash_function(key)  # Получаем индекс для ключа
        if self.table[index] is None:
            # Если ячейка пустая, создаем список с кортежем (ключ, значение)
            self.table[index] = [(key, value)]
        else:
            # Иначе добавляем кортеж в список
            self.table[index].append((key, value))

    def delete(self, obj):
        # Получаем индекс для ключа удаляемого объекта
        index = self.hash_function(obj[0])
        if self.table[index] is not None:
            for item in self.table[index]:
                if item == obj:  # Находим объект по ключу
                    self.table[index].remove(item)  # Удаляем объект из списка
                    break

    def search(self, key):
        index = self.hash_function(key)  # Получаем индекс для ключа
        if self.table[index] is not None:
            for item in self.table[index]:
                if item[0] == key:  # Находим объект по ключу
                    return item[1]  # Возвращаем соответствующее значение
        return None  # Если объект не найден, возвращаем None

    def hash_function(self, key):
        return key % self.size  # Простая хеш-функция для прямой адресации


# Пример использования:
table = DirectAddressTable(10)

table.insert(5, 'apple')
table.insert(15, 'banana')
table.insert(5, 'orange')  # Добавляем элемент с тем же ключом

print(table.search(5))  # Выведет: ['apple', 'orange']
print(table.search(15))  # Выведет: 'banana'

table.delete((5, 'apple'))  # Удаляем элемент по указателю
print(table.search(5))  # Выведет: ['orange']
