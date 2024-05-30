class Node:
    # Инициализация узла
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.node_height = 1


class BalancedTree:
    # Инициализация АВЛ дерева
    def __init__(self):
        self.head = None

    # Публичный метод для добавления узла в дерево
    def add(self, data):
        node_to_add = Node(data)
        self._add_node(node_to_add)

    # Вставка узла в дерево
    def _add_node(self, node_to_add):
        if self.head is None:
            self.head = node_to_add
        else:
            self._add_node_helper(node_to_add, self.head)

    # Вспомогательный метод для рекурсивного добавления узла
    def _add_node_helper(self, node_to_add, current_node):
        if node_to_add.data < current_node.data:
            if current_node.left_child is None:
                current_node.left_child = node_to_add
            else:
                self._add_node_helper(node_to_add, current_node.left_child)
        else:
            if current_node.right_child is None:
                current_node.right_child = node_to_add
            else:
                self._add_node_helper(node_to_add, current_node.right_child)

        # Обновляем высоту текущего узла
        self._update_node_height(current_node)
        # Балансируем дерево
        self._rebalance(current_node)

    # Обновление высоты узла
    def _update_node_height(self, current_node):
        current_node.node_height = 1 + max(self._get_node_height(current_node.left_child),
                                           self._get_node_height(current_node.right_child))

    # Получение высоты узла
    def _get_node_height(self, node):
        if node is None:
            return 0
        return node.node_height

    # Проверка и исправление баланса дерева
    def _rebalance(self, current_node):
        balance = self._get_balance(current_node)

        if balance > 1:
            if self._get_balance(current_node.left_child) < 0:
                self._rotate_left(current_node.left_child)
            self._rotate_right(current_node)
        elif balance < -1:
            if self._get_balance(current_node.right_child) > 0:
                self._rotate_right(current_node.right_child)
            self._rotate_left(current_node)

    # Получение баланса узла
    def _get_balance(self, node):
        if node is None:
            return 0
        return self._get_node_height(node.left_child) - self._get_node_height(node.right_child)

    # Левый поворот
    def _rotate_left(self, node):
        temp = node.right_child
        node.right_child = temp.left_child
        temp.left_child = node

        self._update_node_height(node)
        self._update_node_height(temp)

    # Правый поворот
    def _rotate_right(self, node):
        temp = node.left_child
        node.left_child = temp.right_child
        temp.right_child = node

        self._update_node_height(node)
        self._update_node_height(temp)

    # Поиск узла по его индексу (номеру)
    def find_by_index(self, index):
        current_node = self.head
        counter = 1

        while current_node is not None:
            if counter == index:
                return current_node.data
            elif index < counter:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child

            counter += 1

        return None

    # Публичный метод для вывода дерева в порядке инфиксного обхода
    def print_in_order(self):
        self._print_in_order_helper(self.head)

    # Вспомогательный метод для рекурсивного инфиксного обхода
    def _print_in_order_helper(self, node):
        if node is not None:
            self._print_in_order_helper(node.left_child)
            print(node.data)
            self._print_in_order_helper(node.right_child)


# Создать сбалансированное дерево
balanced_tree = BalancedTree()

# Добавить значения в дерево
balanced_tree.add(13)
balanced_tree.add(6)
balanced_tree.add(18)
balanced_tree.add(2)
balanced_tree.add(17)
balanced_tree.add(7)

print("Дерево:")
balanced_tree.print_in_order()

# Поиск узла по его индексу
index = 1
value = balanced_tree.find_by_index(index)
if value is not None:
    print(f"Значение узла под индексом {index}: {value}")
else:
    print(f"Узел под индексом {index} не найден")
