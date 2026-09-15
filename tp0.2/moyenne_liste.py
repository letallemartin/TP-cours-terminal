def moyenne(liste):
	moyenne = 0
	for i in range(len(liste)):
		moyenne += liste[i]
	return moyenne / (i  + 1)
liste = [10, 5, 2, 3]
print(moyenne(liste))
