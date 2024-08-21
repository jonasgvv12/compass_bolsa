def my_map(lista, f):
    return [f(x) for x in lista]
    
def potenciacao(x):
    return x ** 2
    
lista_entrada = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
calculo = my_map(lista_entrada, potenciacao)

print(calculo)