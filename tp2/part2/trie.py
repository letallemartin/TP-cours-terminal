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
    n = 0
    for i in range(1, len(liste)):
        j = i
        while j > 0 and liste[j] < liste[j - 1]:
            liste[j], liste[j - 1] = liste[j - 1], liste[j]
            j -= 1
            n += 1

    return liste, n

def trie_fusion(liste):
	if len(liste) > 1:
		demi = len(liste) // 2
		gauche = trie_fusion(liste[demi:])
		droite = trie_fusion(liste[:demi])

		i = 0
		j = 0
		k = 0
		while len(gauche) > i and len(droite) > j:
			if gauche[i] < droite[j]:
				liste[k] = gauche [i]
				i += 1
			else:
				liste[k] = droite [j]
				j += 1
			k += 1
		
		while len(gauche) > i:
			liste[k] = gauche [i]
			i += 1
			k += 1
		while len(droite) > j:
			liste[k] = droite [j]
			j += 1
			k += 1
	return liste





tab = [5, 2, 8, 1, 4, 7, 3]
print(trie3(tab))
# print(trie_fusion(tab))
# print(trie3(tab))