def product(smaller, bigger):
    smaller, bigger = (smaller, bigger) if smaller < bigger else (bigger, smaller)
    print(smaller, bigger)
    return product_helper(smaller, bigger)

def product_helper(smaller, bigger):
    if smaller == 1:
        return bigger
    side2 = 0
    if smaller % 2 == 1:
        side2 = bigger
    side1 = product_helper(smaller//2, bigger)
    side2 += side1
    print(smaller, bigger, side1, side2)
    return side1 + side2

print(product(12,100))
