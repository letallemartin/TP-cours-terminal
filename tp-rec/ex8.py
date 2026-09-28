def suite_recurcive(n):
    if  n > 0:
        return 3 * suite_recurcive(n - 1)
    return 2

def suite_iter(n):
    res = 2
    while n > 0:
        res = 3 * res
        n -= 1
    return res

print(suite_iter(10))
print(suite_recurcive(10))