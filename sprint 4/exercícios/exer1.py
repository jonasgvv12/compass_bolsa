with open('number.txt', 'r') as file:
    numeros = list(map(int, file))
    
pares = list(filter(lambda x: x % 2 == 0, numeros))
pares_arrumados = sorted(pares, reverse=True)
top5_pares = pares_arrumados[:5]
soma =  sum(top5_pares)

print(top5_pares)
print(soma)