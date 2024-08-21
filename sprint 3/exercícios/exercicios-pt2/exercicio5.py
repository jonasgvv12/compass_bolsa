def remover_duplicados(lista):
    return list(set(lista))
    
lista = ['abc', 'abc', 'abc', '123', 'abc', '123', '123']
lista_nova = remover_duplicados(lista)

print(lista_nova)