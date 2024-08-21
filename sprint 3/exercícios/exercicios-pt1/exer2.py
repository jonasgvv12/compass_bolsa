numeros = []
for i in range(3):
    numero = int(i + 1)
    numeros.append(numero)
    
for numero in numeros:
    if numero % 2 == 0:
        print(f"Par:", numero)
    else:
        print(f"Ímpar:", numero)