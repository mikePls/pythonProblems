class Node:
    def __init__(self, value=None, left_node=None, right_node=None):
        self.value = value
        self.previous = left_node
        self.next = right_node


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_back(self, val):
        new_node = Node(value=val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node

    def add_to_front(self, val):
        new_node = Node(value=val)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node

    def insert_after(self, target, val):
        current = self.head
        while current is not None:
            if current.value == target:
                if current.next is None:
                    self.add_to_back(val)
                    break
                new_node = Node(value=val, left_node=current, right_node=current.next)
                current.next.previous = new_node
                current.next = new_node
                break
            current = current.next
            if current is None:
                print('Target not found')

    def traverse(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.value)
            current_node = current_node.next

    def sort(self):
        if self.head is None:
            return
        current = self.head
        is_sorted = True
        while current.next is not None:
            if current.value > current.next.value:
                temp = current.value
                current.value = current.next.value
                current.next.value = temp
                is_sorted = False
            current = current.next
        if not is_sorted:
            self.sort()


test_list = DoublyLinkedList()
# test_list.add_to_back(1)
# test_list.add_to_back(2)
# test_list.add_to_front(0)
# test_list.add_to_front(-1)
# test_list.traverse()
#
# test_list.insert_after(2, 3)
# test_list.traverse()
#
# test_list.insert_after(10, 4)

test_list.add_to_back(3)
test_list.add_to_back(1)
test_list.add_to_back(7)
test_list.add_to_front(2)
test_list.add_to_front(0)
test_list.sort()
test_list.traverse()
