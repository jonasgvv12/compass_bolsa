class Ordenadora:
    def __init__(self, listaBaguncada):
        self.listaBaguncada = listaBaguncada
        
    def ordenacaoCrescente(self):
        return sorted(self.listaBaguncada)
        
    def ordenacaoDecrescente(self):
        return sorted(self.listaBaguncada, reverse = True)
        
Crescente = Ordenadora([3,4,2,1,5])
Decrescente = Ordenadora([9,7,6,8])

print(Crescente.ordenacaoCrescente())
print(Decrescente.ordenacaoDecrescente())