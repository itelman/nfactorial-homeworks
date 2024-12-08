from typing import List, Any, Dict, Set, Generator


class StaticArray:
    def __init__(self, capacity: int):
        self.array = [None] * capacity
        self.capacity = capacity

    def set(self, index: int, value: int) -> None:
        if not 0 <= index < self.capacity:
            raise IndexError("Index out of bounds")
        self.array[index] = value

    def get(self, index: int) -> int:
        if not 0 <= index < self.capacity:
            raise IndexError("Index out of bounds")
        return self.array[index]


class DynamicArray:
    def __init__(self):
        self.array = []

    def append(self, value: int) -> None:
        self.array.append(value)

    def insert(self, index: int, value: int) -> None:
        self.array.insert(index, value)

    def delete(self, index: int) -> None:
        if not 0 <= index < len(self.array):
            raise IndexError("Index out of bounds")
        del self.array[index]

    def get(self, index: int) -> int:
        if not 0 <= index < len(self.array):
            raise IndexError("Index out of bounds")
        return self.array[index]


class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def insert(self, position: int, value: int) -> None:
        if position < 0 or position > self._size:
            raise IndexError("Index out of bounds")
        new_node = Node(value)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        else:
            current = self.head
            for _ in range(position - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            if new_node.next is None:
                self.tail = new_node
        self._size += 1

    def delete(self, value: int) -> None:
        current = self.head
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                if current == self.tail:
                    self.tail = prev
                self._size -= 1
                return
            prev = current
            current = current.next
        raise ValueError("Value not found in the list")

    def find(self, value: int) -> Node:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def reverse(self) -> None:
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head, self.tail = self.tail, self.head

    def get_head(self) -> Node:
        return self.head

    def get_tail(self) -> Node:
        return self.tail


class DoubleNode:
    def __init__(self, value: int, next_node=None, prev_node=None):
        self.value = value
        self.next = next_node
        self.prev = prev_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    def append(self, value: int) -> None:
        new_node = DoubleNode(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self._size += 1

    def insert(self, position: int, value: int) -> None:
        if position < 0 or position > self._size:
            raise IndexError("Index out of bounds")
        new_node = DoubleNode(value)
        if position == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if not self.tail:
                self.tail = new_node
        elif position == self._size:
            self.append(value)
            return
        else:
            current = self.head
            for _ in range(position):
                current = current.next
            new_node.next = current
            new_node.prev = current.prev
            if current.prev:
                current.prev.next = new_node
            current.prev = new_node
        self._size += 1

    def delete(self, value: int) -> None:
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
                return
            current = current.next
        raise ValueError("Value not found in the list")

    def find(self, value: int) -> DoubleNode:
        current = self.head
        while current:
            if current.value == value:
                return current
            current = current.next
        return None

    def size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def reverse(self) -> None:
        current = self.head
        while current:
            current.next, current.prev = current.prev, current.next
            current = current.prev
        self.head, self.tail = self.tail, self.head

    def get_head(self) -> DoubleNode:
        return self.head

    def get_tail(self) -> DoubleNode:
        return self.tail


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, value: int) -> None:
        self.items.append(value)

    def dequeue(self) -> int:
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        return self.items.pop(0)

    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.items[0]

    def is_empty(self) -> bool:
        return len(self.items) == 0


class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int) -> None:
        def _insert(node, value):
            if not node:
                return TreeNode(value)
            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        self.root = _insert(self.root, value)

    def delete(self, value: int) -> None:
        def _delete(node, value):
            if not node:
                return node
            if value < node.value:
                node.left = _delete(node.left, value)
            elif value > node.value:
                node.right = _delete(node.right, value)
            else:
                if not node.left:
                    return node.right
                if not node.right:
                    return node.left
                temp = self._find_min(node.right)
                node.value = temp.value
                node.right = _delete(node.right, temp.value)
            return node

        self.root = _delete(self.root, value)

    def search(self, value: int) -> TreeNode:
        def _search(node, value):
            if not node or node.value == value:
                return node
            if value < node.value:
                return _search(node.left, value)
            return _search(node.right, value)

        return _search(self.root, value)

    def inorder_traversal(self) -> list[int]:
        result = []

        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.value)
                _inorder(node.right)

        _inorder(self.root)
        return result

    def size(self) -> int:
        def _size(node):
            if not node:
                return 0
            return 1 + _size(node.left) + _size(node.right)

        return _size(self.root)

    def is_empty(self) -> bool:
        return self.root is None

    def height(self) -> int:
        def _height(node):
            if not node:
                return 0
            return 1 + max(_height(node.left), _height(node.right))

        return _height(self.root)

    def preorder_traversal(self) -> list[int]:
        result = []

        def _preorder(node):
            if node:
                result.append(node.value)
                _preorder(node.left)
                _preorder(node.right)

        _preorder(self.root)
        return result

    def postorder_traversal(self) -> list[int]:
        result = []

        def _postorder(node):
            if node:
                _postorder(node.left)
                _postorder(node.right)
                result.append(node.value)

        _postorder(self.root)
        return result

    def level_order_traversal(self) -> list[int]:
        if not self.root:
            return []
        queue = [self.root]
        result = []
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        return result

    def minimum(self) -> TreeNode:
        return self._find_min(self.root)

    def maximum(self) -> TreeNode:
        return self._find_max(self.root)

    def _find_min(self, node):
        while node and node.left:
            node = node.left
        return node

    def _find_max(self, node):
        while node and node.right:
            node = node.right
        return node

    def is_valid_bst(self) -> bool:
        def _validate(node, low, high):
            if not node:
                return True
            if not (low < node.value < high):
                return False
            return _validate(node.left, low, node.value) and _validate(
                node.right, node.value, high
            )

        return _validate(self.root, float("-inf"), float("inf"))


# Sorting algorithms
def insertion_sort(lst: list[int]) -> list[int]:
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def selection_sort(lst: list[int]) -> list[int]:
    for i in range(len(lst)):
        min_idx = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst


def bubble_sort(lst: list[int]) -> list[int]:
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def shell_sort(lst: list[int]) -> list[int]:
    gap = len(lst) // 2
    while gap > 0:
        for i in range(gap, len(lst)):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst


def merge_sort(lst: list[int]) -> list[int]:
    if len(lst) > 1:
        mid = len(lst) // 2
        left_half = lst[:mid]
        right_half = lst[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                lst[k] = left_half[i]
                i += 1
            else:
                lst[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            lst[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            lst[k] = right_half[j]
            j += 1
            k += 1

    return lst


def quick_sort(lst: list[int]) -> list[int]:
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
