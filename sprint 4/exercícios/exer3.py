from functools import reduce

def calcula_saldo(lancamentos) -> float:
    def calcular_lancamento(lancamento):
        valor, tipo = lancamento
        return valor if tipo == 'C' else -valor
        
    valores_atualizados = map(calcular_lancamento, lancamentos)
    return reduce(lambda saldo, valor: saldo + valor, valores_atualizados, 0.0)