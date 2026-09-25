# def mystere(n):
#     if n == 0:
#         print(n)
#     else:
#         print(n)
#         mystere(n - 1)
#         print(n)

# mystere(5)

def mys2(n):
    if n == 0:
        return n
    else:
        return n + mys2(n - 1)

print(mys2(5))

def factorielle(n):
    if n <= 1:
        return n
    return n * factorielle(n - 1)

print(factorielle(5))

def foix(n):
    if n < 1:
        return n
    return n ** 2 + foix(n - 1)

print(foix(4))

def tab1(tab, i=0):
    if not tab:
        return 0
    return tab[i] + tab1(tab[(1):])

tab = [1,2,3]

print(tab1(tab))