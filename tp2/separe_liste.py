def separe_six(liste):
	liste2 = [[], []]
	for i in liste:
		if len(i) < 6:
			liste2[0].append(i)
		else:
			liste2[1].append(i)
	return liste2
liste = ["aimes", "tu", "manger", "du", "chocolat"]
print(separe_six(liste))