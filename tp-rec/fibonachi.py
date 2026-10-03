def fibo(n,liste):
	global compteur
	compteur += 1
	if n < len(liste):
		return liste[n]
	if n > 1:
		liste.append(fibo(n - 1, liste) + fibo(n - 2, liste))
		return liste[-1]
	return n

compteur = 0

print(fibo(8,[0,1]))

def fibo_iter(n):
	a = 0
	b = 1
	for i in range(n):
		new = a + b
		a = b
		b = new
	return a
print(fibo_iter(8))

# assert fibo(5) == 5
# assert fibo(6) == 8
# assert fibo(15) == 610
# print("c ok !!!")

# print(fibo(10))
# print(fibo(30))

import time
def mesure_temps(n:int) -> float :
    t0 = time.time()
    fibo(n) # Appel de la fonction fibo
    delta_t = time.time() - t0
    return round(delta_t,3)

def seuil(s):
    n = 1
    while mesure_temps(n) < s:
        mesure_temps(n)
        n += 1
    return n - 1

# print(fibo(15))
    
# print(mesure_temps(30))
# print(seuil(10))
def liste_temps(n:int):
    liste_temps = []
    for i in range(1, n - 1):
        liste_temps.append(mesure_temps(i))
    return liste_temps

# import matplotlib.pyplot as plt
def plot_fibo(n):
    y = liste_temps(n)
    plt.xlabel('n')
    plt.ylabel('temps de calcul ( seconds )')
    plt.plot (range(n), y, 'x') # Les points du tracé sont représentés par des croix
    plot_fibo(39)
    plt.show()

# plot_fibo(7)