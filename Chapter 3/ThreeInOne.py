class multi_stack:
    def __init__(self, stack_capacity):
        self.stack_number = 3
        self.val = [0] * self.stack_number * stack_capacity
        self.stack_sizes = [0] * self.stack_number
        self.stack_capacity = stack_capacity

    def push(self, stack_number, value):
        stack_number -= 1
        if self.is_stack_full(stack_number):
            raise Exception('Stack is Full')
        self.val[self.index_of_top(stack_number)] = value
        self.stack_sizes[stack_number] += 1

    def pop(self, stack_number):
        stack_number -= 1
        if self.is_stack_empty(stack_number):
            raise Exception('Stack is Empty')
        temp = self.val[self.index_of_top(stack_number)]
        self.val[self.index_of_top(stack_number)] = 0
        self.stack_sizes[stack_number] -= 1
        return temp
    def peek(self, stack_number):
        stack_number -= 1
        return self.val[self.index_of_top(stack_number)-1]

    def is_stack_full(self, stack_number):
        if self.stack_sizes[stack_number] == self.stack_capacity:
            return True
        else:
            return False

    def is_stack_empty(self, stack_number):
        if self.stack_sizes[stack_number] == 0:
            return True
        else:
            return False

    def index_of_top(self, stack_number):
        offset = (stack_number) * self.stack_capacity + self.stack_sizes[stack_number]
        return offset

def three_in_one():
    newstack = multi_stack(2)
    print(newstack.stack_sizes)
    newstack.push(1,1)
    print(newstack.is_stack_empty(1))
    print(newstack.peek(1))
    print(newstack.pop(1))
    print(newstack.is_stack_empty(1))
three_in_one()

