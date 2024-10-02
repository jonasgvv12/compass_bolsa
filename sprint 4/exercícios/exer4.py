def calcular_valor_maximo(operadores,operandos) -> float:
    def calcular(operando, a, b):
        if operando == '+':
            return a + b
        elif operando == '-':
            return a - b
        elif operando == '/':
            return a / b
        elif operando == '%':
            return a % b
        elif operando == '*':
            return a * b
    resultado = map(lambda x: calcular(x[0], x[1][0], x[1][1]), zip(operadores, operandos))
    return max(resultado)