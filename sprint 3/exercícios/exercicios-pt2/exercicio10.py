class Lampada:
    def __init__(self, estado_inicial):
        self.estado = estado_inicial
        
    def liga(self):
        self.estado = True
        
    def desliga(self):
        self.estado = False
        
    def ligada(self):
        return self.estado
        
    def esta_ligada(self):
        return self.estado
        
lampada = Lampada(False)

lampada.liga()
print(f"A lâmpada está ligada?", lampada.esta_ligada())

lampada.desliga()
print(f"A lâmpada ainda está ligada?", lampada.esta_ligada())