def super_fonction(a) :
    """"
    prend le 1er element de la liste
    et le compare au suivant pour evalue
    le plus petit nb.
    """
    assert len(a) > 1, "error"
    m = a[0]
    n = len(a)
    for i in range(n):
        if a[i] < m :
            m = a[i]
    return m

print(super_fonction([1, 2, 4, 5]))