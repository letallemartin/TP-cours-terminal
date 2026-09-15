def val_negatives(liste):
    l = []
    for i in range(0, len(liste)):
        if liste[i] < 0:
            l.append(liste[i])
    return l

print(val_negatives([2, -4]))
    