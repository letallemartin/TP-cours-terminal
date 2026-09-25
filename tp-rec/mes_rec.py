def somme_tab(tab):
	if not tab:
		return 0
	return tab[0] + somme_tab(tab[1:])

def somme_tab_pos(tab):
	if not tab:
		return 0
	if tab[0] > 0:
		return tab[0] + somme_tab_pos(tab[1:])
	return somme_tab_pos(tab[1:])

print(somme_tab_pos([10,20,-5,20]))

def emecode(n):
	if n < 10:
		return n
	return n % 10 + emecode(n // 10)

print(emecode(5258))

def racine(n):
	if n < 10:
		return n
	return emecode(emecode(n))

print(racine(5515))

def n_eme(rang, n):
	if rang > 1:
		return n_eme(rang - 1, n//10)
	return n % 10
print(n_eme(3, 754))