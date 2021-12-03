def sorrendezes(lista:list[int])->list[int]:
    new_lista=sorted(lista)
    return new_lista

def mini(lista:list[int])->int:
    minimum=min(lista)
    return minimum
def maxi(lista:list[int])->int:
    maximum = max(lista)
    return maximum
def átlag(lista:list[int])->int:
    osszeg=0
    for elem in lista:
        osszeg+=elem
    atlag=(osszeg/len(lista))
    return atlag
def összeg(lista:list[int])->int:
    osszeg = 0
    for elem in lista:
        osszeg += elem
    return osszeg
def minimum(lista:list[int],i:int)->int:
    listam=sorted(lista)
    return listam[i]
def maximum(lista:list[int],i:int)->int:
    listam=sorted(lista,reverse=True)
    return listam[i]
lista=[0,4,2,1,3]
print(sorrendezes(lista))
print(mini(lista))
print(maxi(lista))
print(átlag(lista))
print(összeg(lista))
print(minimum(lista,1))
print(maximum(lista,1))
