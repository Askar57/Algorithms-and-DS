class HashTable:
    def __init__(self):
        # Константы для хэш-функции и размера таблицы
        self.A = 31
        self.P = 300007
        # Создание таблицы с пустыми списками
        self.table = [[] for _ in range(self.P)]

    def hash_function(self, s):
        # Хэш-функция для вычисления индекса по ключу
        h = 0
        for ch in s:
            h = (h * self.A + ord(ch)) % self.P
        return h

    def put(self, key, value):
        # Добавление элемента в таблицу или обновление значения, если ключ уже существует
        index = self.hash_function(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        # Получение значения по ключу
        index = self.hash_function(key)
        for k, v in self.table[index]:
            if k == key:
                print(v)
                return
        # если ключ отсутствует вывод 'null'
        print('null')

    def delete(self, key):
        # Удаление элемента по ключу
        index = self.hash_function(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                del self.table[index][i]
                return
        print('null')

    def cycle_request(self):
        # Цикл для обработки команд до получения команды выхода
        f = True
        while (f):
            r = input().split()  # Получение команды и аргументов
            if r[0] == 'put':
                self.put(r[1], r[2])
            elif r[0] == 'get':
                self.get(r[1])
            elif r[0] == 'delete':
                self.delete(r[1])
            else:
                print('not understand!')
                f = False


hashtable = HashTable()
hashtable.cycle_request()

'''
Пример входных данных:
put hello world
put name ilya
get hello
get ilya
delete hello
get hello
get name
put name vasya
get name
'''
