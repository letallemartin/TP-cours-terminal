def f_multi(a, b):
	if b <= 1:
		return a
	return a + f_multi(a, b - 1)

# print(f_multi(1, 6))

def nettoie(liste):
	if len(liste) == 0:
		return []
	if len(liste) == 1:
		return [liste[0]]
	if liste[0] == liste[1]:
		return nettoie(liste[1:])
	return [liste[0]] + nettoie(liste[1:])

def nettoie_rec(liste):
	i = 0
	if len(liste) <= 1:
		return liste
	while i < len(liste) - 1:
		if liste[i] == liste[i + 1]:
			liste.pop(i)
		else:
			i += 1
	return liste
# print(nettoie_rec([1, 1, 2, 6, 6, 6, 8, 8, 9, 10]))

def Syracuse(n):
	if n <= 1:
		return [n]
	if n % 2 == 0:
		return [n] + Syracuse(n // 2)
	elif n % 2 == 1:
		return [n] + Syracuse(3*n + 1)

# print(Syracuse(6))

def temps_vol(n):
	if n <= 1:
		return 0
	if n % 2 == 0:
		return 1 + temps_vol(n // 2)
	elif n % 2 == 1:
		return 1 + temps_vol(3*n + 1)


def altitude_max1(n):
	if n <= 1:
		return n
	if n % 2 == 0:
		return max(n, altitude_max1(n // 2))
	elif n % 2 == 1:
		return max(n, altitude_max1(3*n + 1))

def altitude_max2(n, max = 0):
	if n > max:
		max = n
	if n <= 1:
		return max
	if n % 2 == 0:
		return altitude_max2(n // 2, max)
	elif n % 2 == 1:
		return altitude_max2(3*n + 1, max)


def trouver_intrus(tab, g, d):
	"""Renvoie la valeur de l'intrus situé entre les indices g et d dans le tableau tab où :
	tab vérifie les conditions de l'exercice,
	g et d sont des multiples de 3."""
	if g == d:
		return tab[g]
	else: 
		nombre_de_triplets = (d - g) // 3
		indice = g + 3 * (nombre_de_triplets // 2)
		if tab[indice] == tab[indice + 1]:
			return trouver_intrus(tab, indice + 3, d)
		else:
			return trouver_intrus(tab, g, indice)

print(trouver_intrus([8, 5, 5, 5, 9, 9, 9, 18, 18, 18, 3, 3, 3], 0, 12))