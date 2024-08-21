class Calculo:
    def soma(self, x, y):
        return x + y   
    def subtrair(self, x, y):
        return x - y
        
Calcular = Calculo()
x = 4
y = 5

print(f"Somando: {x} + {y} =  {Calcular.soma(x, y)}")
print(f"subtraindo: {x} - {y} =  {Calcular.subtrair(x, y)}")