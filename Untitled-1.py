def fonction(n):
    somme = 0
    for i in range(1, n + 1):
        somme += i
    print(somme)



def somme_gauss(n):
    return n*(n+1)//2

fonction(50000000)
print(somme_gauss(50000000))





# int fonction(n)
# {
#     int somme;
    
#     somme = 0;
#     while (n > 0)
#     {
#         n--;
#         somme += n;
#     }
#     return (somme);
# }
