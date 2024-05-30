class BitVectorSet:
    def __init__(self, size):
        self.size = size
        # Создаем битовый вектор заданного размера и инициализируем его False
        self.bit_vector = [False] * size

    def _hash(self, key):
        # Простая хеш-функция для преобразования ключа в индекс битового вектора
        return hash(key) % self.size

    def add(self, key):
        index = self._hash(key)  # Получаем индекс в битовом векторе для ключа
        # Устанавливаем бит в этом индексе как True
        self.bit_vector[index] = True

    def contains(self, key):
        index = self._hash(key)  # Получаем индекс в битовом векторе для ключа
        # Возвращаем значение бита в этом индексе
        return self.bit_vector[index]

    def remove(self, key):
        index = self._hash(key)  # Получаем индекс в битовом векторе для ключа
        self.bit_vector[index] = False  # Сбрасываем бит в этом индексе


# Пример использования
bit_vector_set = BitVectorSet(10)  # Создаем битовую хеш-таблицу размером 10

# Добавляем элементы в множество
bit_vector_set.add("apple")
bit_vector_set.add("banana")
bit_vector_set.add("orange")

# Проверяем наличие элементов в множестве
print(bit_vector_set.contains("apple"))  # True
print(bit_vector_set.contains("grape"))  # False

# Удаляем элемент из множества
bit_vector_set.remove("banana")

# Проверяем изменения
print(bit_vector_set.contains("banana"))  # False
