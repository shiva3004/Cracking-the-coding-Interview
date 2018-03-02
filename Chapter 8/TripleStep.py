def triple_steps(n):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    return triple_steps(n-1) + triple_steps(n-2) + triple_steps(n-3)

def triple_steps_dp(n):
    memory = [0] * (n+1)
    print(memory)
    return get_triple_steps_in_dp(n, memory)

def get_triple_steps_in_dp(n, memory):
    if n < 0:
        return 0
    if n <= 1:
        return 1
    if memory[n] > 0:
        return memory[n]
    memory[n] = get_triple_steps_in_dp(n-1, memory) + get_triple_steps_in_dp(n-2, memory) + get_triple_steps_in_dp(n-3, memory)
    return memory[n]
print(triple_steps_dp(28))
