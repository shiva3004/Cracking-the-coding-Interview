def getPowerSet(set):
    if len(set) == 1:
        return [set]
    ret_set = getPowerSet(set[:-1])
    val = set[-1]
    res_set = []
    print(ret_set)
    for i in range(len(ret_set)):
        t = ret_set[i].copy()
        t.append(val)
        res_set.append(t)
    res_set.append([val])
    return res_set + ret_set

set = ['a','b','c']

print(getPowerSet(set))
