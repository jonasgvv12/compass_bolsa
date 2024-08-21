class Aviao:
    def __init__(self, modelo, velocidade_maxima, capacidade):
        self.modelo = modelo
        self.velocidade_maxima = velocidade_maxima
        self.cor = "Azul"
        self.capacidade = capacidade
        
    def __str__(self):
        return f"Modelo {self.modelo} velocidade máxima {self.velocidade_maxima} km/h: capacidade para {self.capacidade} passageiros: Cor {self.cor}"
        
info_avioes = [
    Aviao("BOIENG456", 1500, 400),
    Aviao("Embraer Praetor 600", 863, 14),
    Aviao("Antonov An-2", 258, 12)
]

for Aviao in info_avioes:
    print(Aviao)