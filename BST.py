# Реализация бинарного дерева поиска

class BSTNode:  # одна вершина дерева
    def __init__(self, value=None):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):  # функция вставки нового элемента в дерево
        if not self.value:
            self.value = value
            return

        if self.value == value:
            return

        if value < self.value:
            if self.left:
                self.left.insert(value)
                return
            self.left = BSTNode(value)
            return

        if self.right:
            self.right.insert(value)
            return
        self.right = BSTNode(value)

    def get_min(self):  # поиск минимального
        current = self
        while current.left is not None:
            current = current.left
        return current.value

    def get_max(self):  # поиск максимального
        current = self
        while current.right is not None:
            current = current.right
        return current.value

    def delete(self, value):  # удаление определенного элемента
        if self is None:
            return self
        if value < self.value:
            self.left = self.left.delete(value)
            return self
        if value > self.value:
            self.right = self.right.delete(value)
            return self
        if self.right is None:
            return self.left
        if self.left is None:
            return self.right
        min_larger_node = self.right
        while min_larger_node.left:
            min_larger_node = min_larger_node.left
        self.value = min_larger_node.val
        self.right = self.right.delete(min_larger_node.val)
        return self

    def exists(self, value):  # есть ли элемент в дереве
        if value == self.value:
            print(f"Value {value} exists in the tree.")
            return True

        if value < self.value:
            if self.left is None:
                print(f"Value {value} doesn't exist in the tree.")
                return False
            return self.left.exists(value)

        if self.right is None:
            print(f"Value {value} doesn't exist in the tree.")
            return False
        return self.right.exists(value)

    def inorder(self, values):  # вывод элементов в порядке возрастания
        if self.left is not None:
            self.left.inorder(values)
        if self.value is not None:
            values.append(self.value)
        if self.right is not None:
            self.right.inorder(values)
        return values

    def postorder(self, values):  # в порядке убывания

        if self.right is not None:
            self.right.postorder(values)
        if self.value is not None:
            values.append(self.value)
        if self.left is not None:
            self.left.postorder(values)
        return values


nums = [12, 6, 18, 19, 21, 11, 3, 5, 4, 24, 18]
bst = BSTNode()
for num in nums:
    bst.insert(num)

print("postorder:")
print(bst.postorder([]))
print("###")

print("inorder:")
print(bst.inorder([]))
print("###")

bst.delete(18)
print("inorder:")
print(bst.inorder([]))
print("###")

print(f"MIN: {bst.get_min()}; MAX: {bst.get_max()}")

print(bst.exists(15))
print(bst.exists(19))
print(bst.exists(18))
bst.exists(228)
