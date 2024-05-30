# Би-Дерево
# 1) Поиск элемента
# 2) Предшествующий
# 3) Последующий
# 4) Минимальный
# 5) Максимальный


import matplotlib.pyplot as plt


class Node:
    def __init__(self, leaf=True):
        self.leaf = leaf  # Показывает, является ли узел листовым
        self.keys = []    # Список ключей в узле
        self.child = []   # Список дочерних узлов


class BTree:
    def __init__(self, t):
        self.root = Node(True)  # Создание корневого узла
        self.t = t              # Параметр минимальной степени B-дерева

    # Метод вставки ключа в дерево
    def insert(self, key):
        root = self.root
        # Если корень заполнен, выполняется разделение корня
        if len(root.keys) == (2 * self.t) - 1:
            new_root = Node(False)
            new_root.child.insert(0, root)
            self.split_child(new_root, 0)
            self.root = new_root
            self.insert_non_full(new_root, key)
        else:
            self.insert_non_full(root, key)

    # Вспомогательный метод для вставки ключа в неполный узел
    def insert_non_full(self, x, k):
        i = len(x.keys) - 1  # индекс последнего ключа в узле x
        if x.leaf:
            # Вставка ключа в листовой узел
            x.keys.append(0)
            while i >= 0 and k < x.keys[i]:
                x.keys[i + 1] = x.keys[i]
                i -= 1
            x.keys[i + 1] = k
        else:
            # Вставка ключа во внутренний узел
            while i >= 0 and k < x.keys[i]:
                i -= 1
            i += 1
            if len(x.child[i].keys) == (2 * self.t) - 1:
                # Если дочерний узел уже полон то делим его корень
                self.split_child(x, i)
                if k > x.keys[i]:
                    i += 1
            self.insert_non_full(x.child[i], k)

    # Метод разделения узла
    def split_child(self, x, i):
        t = self.t
        y = x.child[i]
        z = Node(y.leaf)
        x.child.insert(i + 1, z)
        x.keys.insert(i, y.keys[t - 1])
        z.keys = y.keys[t:(2 * t) - 1]
        y.keys = y.keys[0:t-1]
        if not y.leaf:
            z.child = y.child[t:2*t]
            y.child = y.child[0:t-1]

    # Метод поиска ключа в дереве
    def search(self, k, x=None):
        if x is not None:
            i = 0
            while i < len(x.keys) and k > x.keys[i]:
                i += 1
            if i < len(x.keys) and k == x.keys[i]:
                return True
            elif x.leaf:
                return False
            else:
                return self.search(k, x.child[i])
        else:
            return self.search(k, self.root)

    # Визуализация B-дерева
    def plot_btree_recursive(self, ax, node, x, y, dx):
        if node is None:
            return None

        ax.text(x, y, str(node.keys), bbox={
                'facecolor': 'red', 'alpha': 0.5, 'pad': 15})
        if not node.leaf:
            for i, child in enumerate(node.child):
                ax.plot([x, x + (i - 1) * dx], [y - 1, y - 2], 'k-')
                self.plot_btree_recursive(
                    ax, child, x + (i - 1) * dx, y - 2, dx / 1.7)

    # Отображение B-дерева
    def plot_btree(self):
        if self.root is None:
            print("Дерево пустое")
            return

        fig, ax = plt.subplots()
        ax.axis('off')
        self.plot_btree_recursive(ax, self.root, 0, 0, 10)
        plt.show()

    # Нахождение минимального ключа в дереве
    def find_min(self):
        node = self.root
        while not node.leaf:
            node = node.child[0]
        return node.keys[0]

    # Нахождение максимального ключа в дереве
    def find_max(self):
        node = self.root
        while not node.leaf:
            node = node.child[-1]
        return node.keys[-1]

    # Определение высоты дерева
    def height(self, node=None):
        if node is None:
            node = self.root
        if node is None:
            return -1
        if node.leaf:
            return 1
        return 2 + self.height(node.child[0])


# Пример использования
if __name__ == '__main__':
    B = BTree(2)  # Создание B-дерева с t=3
    keys = [10, 5, 7, 16, 13, 2, 20, 1]
    for key in keys:
        B.insert(key)

    print()
    print("Поиск числа 7:", B.search(7))
    print("Поиск числа 15:", B.search(15))
    print()
    print("Поиск Минимального:", B.find_min())
    print("Поиск Максимального:", B.find_max())
    print("Высота дерева:", B.height())

    B.plot_btree()
