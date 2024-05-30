'''Определение узла дерева по его номеру.'''


class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

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
            self.size = 1
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
            self.size += 1

        return obj

    def get_node_by_index(self, index):
        '''Функция для получения узла дерева по его порядковому номеру'''
        if index < 0 or index >= self.size:
            return None

        node = self.root
        current_index = 0
        while node:
            left_size = self.get_size(node.left)
            if index == current_index + left_size:
                return node
            elif index < current_index + left_size:
                node = node.left
            else:
                node = node.right
                current_index += left_size + 1

    def get_size(self, node):
        '''Функция для получения размера поддерева'''
        if node is None:
            return 0
        return 1 + self.get_size(node.left) + self.get_size(node.right)

    def show_tree(self, node):
        '''Функция для отображения дерева по порядку'''
        if node is None:
            return

        self.show_tree(node.left)
        print(node.data)
        self.show_tree(node.right)


v = [10, 5, 7, 16, 13, 2, 20]

t = Tree()
for x in v:
    t.append(Node(x))

# Пример использования:
for i in range(t.size):
    node = t.get_node_by_index(i)
    print(f"Узел {i}: {node.data}")
