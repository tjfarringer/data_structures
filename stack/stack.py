# Stack:  the element deleted is the one most recently inserted.  Last-in first-out.
##  Insert -> "push".  Delete -> "pop".


# Stack:  the element deleted is the one most recently inserted.  Last-in first-out.
##  Insert -> "push".  Delete -> "pop".


class Stack():
    def __init__(self, max_elements):
        self.top = 0
        self.stack = [None] * 10

    def empty(self):
        '''
        Checks if the stack is empty
        :return:
        '''
        if self.stack[self.top] is None:
            return True
        else:
            return False

    def push(self, value):
        '''
        Insert new value
        :return:
        '''
        if not self.empty():
            self.top += 1

        self.stack[self.top] = value

    def pop(self):
        '''
        Returns the last added value.  Notice that it is not removed.  The element remains in the overall list.
        :return:
        '''
        if self.empty():
            raise ValueError('Error:  The stack is empty!')
        else:
            self.top -= 1
            return self.stack[self.top + 1]