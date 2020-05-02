
class Node():
    def __init__(self, data):
        self.data = data
        # self.prev = prev
        # self.next = next

    def get_data(self):
        return self.data

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.x.next = new_next

    def set_prev(self, new_prev):
        self.x.prev = new_prev


class LinkedList():
    def __init__(self, head=None):
        self.head = head

    def list_search(self, k):
        '''
        Note that this (in the worst case) is O(n).
        :param k:
        :return:
        '''
        current = self.head

        while current is not None and current != k:
            current = current.get_next()

        return current

    def insert_node(self, data):
        new_node = Node(data)
        new_node.set_next(self.head)
        new_node.set_prev(None)

        if self.head is not None:
            self.head.set_prev(new_node)

        self.head = new_node

    def delete_node(self, node):
        if node.get_prev() is not None:
            x.


        new_node = Node(data)
        new_node.set_next(self.head)
        new_node.set_prev(None)

        if self.head is not None:
            self.head.set_prev(new_node)

        self.head = new_node

    def return_size(self):
        current = self.head
        num_nodes = 0

        while current:
            num_nodes += 1
            current = current.get_next()

        return num_nodes








