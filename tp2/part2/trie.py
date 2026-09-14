def trie(liste):
    trie = False
    n = 0
    while trie == False:
        trie = True
        for i in range(len(liste) - 1):
            if liste[i] > liste[i + 1]:
                trie = False
                liste[i], liste[i + 1] = liste[i + 1], liste[i]
            n += 1
    return liste, n

def trie2(liste):
    n = 0
    for i in range(len(liste)):
        for j in range(i + 1, len(liste)):
            if liste[i] > liste[j]:
                liste[i], liste[j] = liste[j], liste[i]
            n += 1
        return liste, n

def trie3(liste): #insertion
    nb = 0
    n = 0
    for i in range(1, len(liste)):
        j = i
        nb = liste[j]
        while liste[j] < liste[j - 1] and j > 0:
            
            liste[j], liste[j - 1] = liste[j - 1], liste[j]
            j -= 1
            n += 1

    return liste, n
                
    
    
tab = [5, 2, 8, 1, 4, 7, 3]
print(trie3(tab))