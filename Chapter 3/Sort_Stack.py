from stack import stack
class sort_the_stack:
    def __init__(self):
        self.sorted_stack = stack()

    def sort_stack(self, new_stack):
        for i in range(new_stack.size()):
            self.push(new_stack.pop())
        return self.sorted_stack

    def push(self, val):
        if self.sorted_stack.size() == 0:
            self.sorted_stack.push(val)
        else:
            temp = self.sorted_stack.peek()
            if val < temp:
                self.sorted_stack.push(val)
            else:
                temp = self.sorted_stack.pop()
                self.push(val)
                self.sorted_stack.push(temp)

    def peek(self):
        return self.sorted_stack.peek()

    def pop(self):
        return self.sorted_stack.pop()



new_stack = stack()
new_stack.push(10)
new_stack.push(2)
new_stack.push(1)
new_stack.push(8)
new_stack.push(1)
new_stack.push(1)

stack1 = sort_the_stack()
stack1.sort_stack(new_stack)


print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
print(stack1.pop())
