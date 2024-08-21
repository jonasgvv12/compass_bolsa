class Passaro:
    def voar(self):
        print("Voando...")
    def emitir_som(self):
        raise NotImplementedError
        
class Pardal(Passaro):
    def emitir_som(self):
        print("Piu Piu")
        
class Pato(Passaro):
    def emitir_som(self):
        print("Quack Quack")

pato = Pato()
pardal = Pardal()

print("Pato")
pato.voar()
print("Pato emitindo som...")
pato.emitir_som()
print("\nPardal")
pardal.voar()
print("Pardal emitindo som...")
pardal.emitir_som