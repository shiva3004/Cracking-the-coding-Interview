class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) == 0:
            raise Exception('Queue is Empty')
        return self.stack.pop()

    def peek(self):
        if len(self.stack) == 0:
            raise Exception('Queue is Empty')
        return self.stack[-1]

    def size(self):
        return len(self.stack)

class MyQueue:
    def __init__(self):
        self.new_stack = Stack()
        self.old_stack = Stack()

    def enqueue(self, item):
        self.new_stack.push(item)

    def dequeue(self):
        if self.new_stack.size() == 0 and self.old_stack.size() == 0:
            raise Exception('Queue is Empty')
        if self.old_stack.size() == 0:
            self.shift_elements()
        return self.old_stack.pop()

    def shift_elements(self):
       for i in range(self.new_stack.size()):
           self.old_stack.push(self.new_stack.pop())

queue = MyQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
