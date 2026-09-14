import random
def make_liste(i):
	liste = [random.randint(0, 100) for i in range(i)]
	return liste

print(make_liste(6))
