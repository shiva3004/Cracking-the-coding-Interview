class three_in_stack:
    def __init__(self, capacity):
        self.stack_size = 3
        self.stack_capacity = capacity
        self.stack_sizes = [0] * self.stack_size
        self.stack_array = [0] * self.stack_size * self.stack_capacity

    def push(self, stack_number, val):
        if self.is_full(stack_number):
            raise Exception('Stack {0} is Full', stack_number)
        self.stack_array[self.get_index(stack_number)] = val
        self.stack_sizes[stack_number] += 1

    def get_index(self, stack_number):
        return stack_number * self.stack_capacity + self.stack_sizes[stack_number]

    def is_full(self, stack_number):
        return self.stack_capacity == self.stack_sizes[stack_number]

    def pop(self, stack_number):
        if self.is_empty(stack_number):
            raise Exception('Cannot pop from the stack number {0}', stack_number)
        temp = self.stack_array[self.get_index(stack_number)-1]
        self.stack_array[self.get_index(stack_number)-1] = 0
        self.stack_sizes[stack_number] -= 1
        return temp

    def is_empty(self, stack_number):
        return self.stack_sizes[stack_number] == 0

    def print(self):
        for each in self.stack_array:
            print(each)


stacks = three_in_stack(3)
stacks.push(0,1)
stacks.push(0,2)
stacks.push(1,4)
stacks.push(2,7)
stacks.print()
print(stacks.is_empty(0))
print(stacks.is_empty(1))
print(stacks.is_empty(2))
print(stacks.pop(0))
print(stacks.pop(0))
print(stacks.pop(1))
print(stacks.pop(2))
print(stacks.is_empty(0))
print(stacks.is_empty(1))
print(stacks.is_empty(2))
