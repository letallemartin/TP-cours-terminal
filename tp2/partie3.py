def polynome(t) :
	# S'il y a plus de 3 éléments, alors on prévient l'utilisateur
	# car la valeur rentrée n'est pas correcte
	if len(t) > 3 :
		raise ValueError("La liste doit contenir 3 éléments.")
	# Si le paramètre rentré n'est pas de type liste, on le dit
	if not(isinstance(t, list)) :
		raise TypeError("TypeError : t doit être une liste.")
	a = t[0]
	b = t[1]
	c = t[2]
	print(f"Polynome : {a}x² + {b}x + {c}")

polynome([3, 2, 10])
polynome(3)
polynome([1, 2, 3, 4])


def moyenne(liste) :
	somme = 0
	if not(isinstance(liste, list)):
		raise TypeError("ce n'est pas une liste")
	for i in range(len(liste)) :
		if not(isinstance(liste[i], int)):
			raise TypeError("ce n'est pas un nb correct")
		somme += liste[i]
	return somme / len(liste)

print(moyenne([1, 2, 3, 4]))
# moyenne()