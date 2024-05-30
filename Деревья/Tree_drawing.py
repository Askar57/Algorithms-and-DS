import matplotlib.pyplot as plt

'''Рисование дерева'''


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

    def _plot_tree_recursive(self, ax, node, x, y, dx):
        if node is None:
            return

        ax.text(x, y, str(node.data), bbox={
                'facecolor': 'red', 'alpha': 0.5, 'pad': 15})
        if node.left:
            ax.plot([x, x - dx], [y - 1, y - 2], 'k-')
            self._plot_tree_recursive(
                ax, node.left, x - dx - 1, y - 2, dx / 1.7)
        if node.right:
            ax.plot([x, x + dx], [y - 1, y - 2], 'k-')
            self._plot_tree_recursive(
                ax, node.right, x + dx + 1, y - 2, dx / 1.7)

    def plot_tree(self):
        '''Функция для отображения дерева'''
        if self.root is None:
            print("Дерево пустое")
            return

        fig, ax = plt.subplots()
        ax.axis('off')
        self._plot_tree_recursive(ax, self.root, 0, 0, 10)
        plt.show()


v = [10, 5, 7, 16, 13, 2, 20]

t = Tree()
for x in v:
    t.append(Node(x))

t.plot_tree()
