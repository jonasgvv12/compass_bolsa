def soma_string(valoresString):
    return sum(int(x) for x in valoresString.split(","))
    
valoresString = "1,3,4,6,10,76"
print(soma_string(valoresString))