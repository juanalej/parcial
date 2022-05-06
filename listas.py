lista=["juan","pedro","Natalia","4","6"]
j=len(lista)
print("la lista es:",lista)
print("la cantidad de elemntos de la lista son:",j)
def invertirLista (i):
    invertir=[]
    a=len(i)-1
    while a>=0:
        invertir.append(i[a])
        a-=1
    return invertir
print("la lista invertida es",invertirLista(lista))
