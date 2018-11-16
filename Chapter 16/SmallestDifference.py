
def getSmallestDifference(a, b):
    min_difference = float('inf')
    a.sort(); b.sort()
    i = 0; j = 0
    while i < len(a) and j < len(b):
        diff = abs(a[i] - b[j])
        if diff < min_difference:
            min_difference = diff
        if a[i] < b[j]:
            i += 1
        else:
            j += 1
    return min_difference


a = [1, 2, 11, 15]
b = [4, 12, 19, 127, 235]
ans = getSmallestDifference(a, b)

print(ans)
