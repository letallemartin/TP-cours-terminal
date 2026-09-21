dico ={'a' : 1, 'b' : 2}
dico2 = {'c' : 1, 'd' : 2}
def fonction(dico, dico2):
    for cle, val in dico2.items():
        dico[cle] = val
        
    
    
fonction(dico, dico2)

def fonction2(dico):
    list1 = []
    list2 = []
    for cle,val in dico.items():
        list1.append(cle)
        list2.append(val)
    return list1,list2

print(fonction2(dico))