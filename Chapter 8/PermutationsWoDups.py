def get_permutations(string):
    if len(string) == 0:
        perms = [string]
        return perms
    prev_perms = get_permutations(string[:-1])
    iter = string[-1]
    perms = []
    for s in prev_perms:
        for i in range(len(s)+1):
            v = s[:i] + iter + s[i:]
            perms.append(v)
    return perms

perms = get_permutations('abcdef')
print(perms)
print(len(perms))
