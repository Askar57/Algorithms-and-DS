# 1) Поиск элемента
# 2) Предшествующий
# 3) Последующий
# 4) Минимальный
# 5) Максимальный

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def finder(self, node, parent, value):
        '''Функция для поиска мест расположения новых вершин'''
        if node is None:
            return None, parent, False

        if value == node.data:
            return node, parent, True  # Значит нашли вершину соответствующую значению value

        if value < node.data:
            if node.left:
                # Ищем вершину в левом узле
                return self.finder(node.left, node, value)

        if value > node.data:
            if node.right:
                # Ищем вершину в правом узле
                return self.finder(node.right, node, value)

        return node, parent, False  # Значит не нашли вершину соответствующую значению value

    def append(self, obj):
        '''Функция для добавления вершин в дерево'''
        if self.root is None:
            self.root = obj
            return obj

        s, p, fl_find = self.finder(self.root, None, obj.data)

        if not fl_find and s:
            # Если добавляемое значение еще не присутствует в дереве и корень дерева существует
            if obj.data < s.data:
                # Если добавляемое значение меньше значения в родительском узле
                # то новая вершина добавляет в левую ветвь
                s.left = obj
            else:
                # Если больше, то в правую
                s.right = obj

        return obj

    def show_tree(self, node):
        '''Функция для отображения дерева по порядку'''
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)

    def find(self, value):
        """Поиск элемента"""
        node, _, found = self.finder(self.root, None, value)
        return node if found else None

    def predecessor(self, value):
        """Поиск предшествующего"""
        node = self.find(value)
        if node is None:
            return None
        if node.left:
            return self.maximum(node.left)
        else:
            parent = self.find_parent(value)
            while parent and node == parent.left:
                node = parent
                parent = self.find_parent(node.data)
            return parent

    def successor(self, value):
        """Поиск последующего"""
        node = self.find(value)
        if node is None:
            return None
        if node.right:
            return self.minimum(node.right)
        else:
            parent = self.find_parent(value)
            while parent and node == parent.right:
                node = parent
                parent = self.find_parent(node.data)
            return parent

    def minimum(self, node):
        """Поиск минимального"""
        while node.left:
            node = node.left
        return node

    def maximum(self, node):
        """Поиск максимального"""
        while node.right:
            node = node.right
        return node

    def find_parent(self, value):
        """Поиск родителя узла с заданным значением"""
        _, parent, _ = self.finder(self.root, None, value)
        return parent

    def height(self, node):
        """Вычисление высоты дерева"""
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)
            return max(left_height, right_height) + 1


v = [10, 5, 7, 16, 13, 2, 20]

t = Tree()
for x in v:
    t.append(Node(x))

t.show_tree(t.root)

print()
print("Поиск элемента:", t.find(2).data)
print("Поиск Предшествующего:", t.predecessor(2).data)
print("Поиск Последующего:", t.successor(2).data)
print("Поиск Минимального:", t.minimum(t.root).data)
print("Поиск Максимального:", t.maximum(t.root).data)
print("Высота дерева:", t.height(t.root))
