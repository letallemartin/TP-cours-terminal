
memo = {}
def fibo_opt(n):
    if n in memo:
        return memo[n]
    if n == 0:
        resultat = 0
    elif n == 1:
        resultat = 1
    else:
        resultat = fibo_opt(n - 1) + fibo_opt(n - 2)
    memo[n] = resultat
    return resultat


def fibo1(n):
	global compteur
	compteur += 1
	if n <= 1:
		return n
	return fibo1(n - 1) + fibo1(n - 2)

# compteur = 0
# print(fibo1(10,[0,1]))
# print(compteur)


def fibo_iter(n):
	a = 0
	b = 1
	for i in range(n):
		new = a + b
		a = b
		b = new
	return a
# print(fibo_iter(8))

import time
def mesure_temps(n:int) -> float :
    t0 = time.time()
    fibo1(n) # Appel de la fonction fibo
    delta_t = time.time() - t0
    return round(delta_t,3)
# print(mesure_temps(1O))

def seuil(s):
    n = 1
    while mesure_temps(n) < s:
        mesure_temps(n)
        n += 1
    return n - 1

# print(fibo(15))
    
print(mesure_temps(59))
# print(seuil(10))
def liste_temps(n:int):
    liste_temps = []
    for i in range(1, n - 1):
        liste_temps.append(mesure_temps(i))
    return liste_temps

import matplotlib.pyplot as plt
def plot_fibo(n):
    y = liste_temps(n)
    plt.xlabel('n')
    plt.ylabel('temps de calcul ( seconds )')
    plt.plot (range(n), y, 'x') # Les points du tracé sont représentés par des croix
# plot_fibo(39)
# plt.show()

# assert fibo(5) == 5
# assert fibo(6) == 8
# assert fibo(15) == 610
# print("c ok !!!")

# print(fibo(10))
# print(fibo(30))

# def fibo(n,liste):
# 	global compteur
# 	compteur += 1
# 	if n < len(liste):
# 		return liste[n]
# 	if n > 1:
# 		liste.append(fibo(n - 1, liste) + fibo(n - 2, liste))
# 		return liste[-1]
# 	return n

# compteur = 0
# print(fibo(5,[0,1]))
# print(compteur)