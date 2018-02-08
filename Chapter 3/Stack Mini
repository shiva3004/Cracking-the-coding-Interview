from stack import stack ## use this stack to store the minimun elements
class stack_mini:
    class stack_node:
        def __init__(self, val):
            self.val = val
            self.next = None
    top = None
    stack_min = stack()
    def push(self, val):
        if self.top is None:
            self.top = self.stack_node(val)
            self.stack_min.push(val)
        else:
            if val < self.stack_min.peek():
                self.stack_min.push(val)
            node = self.stack_node(val)
            node.next = self.top
            self.top = node

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        temp = self.top
        self.top = self.top.next
        if temp.val == self.stack_min.peek():
            self.stack_min.pop()
        return temp.val

    def is_empty(self):
        return self.top is None

    def min(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self.stack_min.peek()

stack = stack_mini()
stack.push(4)
stack.push(5)
stack.push(1)
stack.push(7)
stack.push(2)
print(stack.min())
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.min())
