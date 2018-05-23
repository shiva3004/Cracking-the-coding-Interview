def multiply(val, n):
    if n == 0:
        return 0
    return val + multiply(val, n-1)


def multiply_rec(val, n):
    if n == 0:
        return 0
    elif n == 1:
        return val
    n_c = n >> 1
    side1 = multiply_rec(val, n_c)
    side2 = side1
    if n % 2 == 1:
        side2 = multiply_rec(val, n-n_c)
    return side1 + side2


def multiply_dp_helper(val, n, memory):
    if n == 0:
        return 0
    elif n == 1:
        return val
    elif n in memory.keys():
        return memory[n]
    n_c = n >> 1
    side1 = multiply_dp_helper(val, n_c, memory)
    side2 = side1
    memory[n_c] = side1
    if n%2 == 1:
        side2 = multiply_dp_helper(val, n-n_c, memory)
    return side1 + side2


def multiply_dp(val, n):
    memory = {}
    return multiply_dp_helper(val, n, memory)


def multiply_quicker(val, n):
    if n == 0:
        return 0
    elif n ==1 :
        return val
    odd_value = 0
    if n%2 == 1:
        odd_value = val
        n -= 1
    n_c = n >> 1
    side1 = multiply_quicker(val, n_c)
    return side1 + side1 + odd_value




print(multiply_quicker(7, 10))
