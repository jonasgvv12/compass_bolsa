lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

def dividirLista(lista):
    tamanho = len(lista)
    divisao = int(tamanho / 3)
    lista1 = lista[:divisao]
    lista2 = lista[divisao:divisao*2]
    lista3 = lista[divisao*2:]
    return lista1, lista2, lista3


lista1, lista2, lista3 = dividirLista(lista)

print(lista1, lista2, lista3)
