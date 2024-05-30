class AVLNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1


class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = AVLNode(value)
        self._insert(new_node)

    def _insert(self, new_node):
        if self.root is None:
            self.root = new_node
        else:
            self._insert_helper(new_node, self.root)

    def _insert_helper(self, new_node, current_node):
        if new_node.value < current_node.value:
            if current_node.left is None:
                current_node.left = new_node
            else:
                self._insert_helper(new_node, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = new_node
            else:
                self._insert_helper(new_node, current_node.right)

        self._update_heights(current_node)
        self._balance(current_node)

    def _update_heights(self, current_node):
        current_node.height = 1 + \
            max(self._get_height(current_node.left),
                self._get_height(current_node.right))

    def _get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def _balance(self, current_node):
        balance_factor = self._get_balance_factor(current_node)

        if balance_factor > 1:
            if self._get_balance_factor(current_node.left) < 0:
                self._left_rotate(current_node.left)
            self._right_rotate(current_node)
        elif balance_factor < -1:
            if self._get_balance_factor(current_node.right) > 0:
                self._right_rotate(current_node.right)
            self._left_rotate(current_node)

    def _get_balance_factor(self, node):
        if node is None:
            return 0
        else:
            return self._get_height(node.left) - self._get_height(node.right)

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        right_child.left = node

        self._update_heights(node)
        self._update_heights(right_child)

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        left_child.right = node

        self._update_heights(node)
        self._update_heights(left_child)

    def search_by_number(self, number):
        current_node = self.root
        count = 1

        while current_node is not None:
            if count == number:
                return current_node.value
            elif number < count:
                current_node = current_node.left
            else:
                current_node = current_node.right

            count += 1

        return None

    def in_order_traversal(self):
        self._in_order_traversal_helper(self.root)

    def _in_order_traversal_helper(self, node):
        if node is not None:
            self._in_order_traversal_helper(node.left)
            print(node.value)
            self._in_order_traversal_helper(node.right)


# Создать АВЛ-дерево
tree = AVLTree()

# Вставить значения в дерево
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(7)
tree.insert(12)
tree.insert(17)

# Напечатать дерево в порядке инфиксного обхода
print("Дерево в порядке инфиксного обхода:")
tree.in_order_traversal()

# Поиск узла по его номеру без использования рекурсии
number = 4
node_value = tree.search_by_number(number)
if node_value is not None:
    print(f"Значение узла под номером {number}: {node_value}")
else:
    print(f"Узел под номером {number} не найден")
