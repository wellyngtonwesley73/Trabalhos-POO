import math

class Ponto:
    # definição dos métodos
    def __init__(self, x, y):
        # definição dos atributos
        self.x = x
        self.y = y

    def exibir(self):
        x = self.x
        y = self.y
        print(f'{x=}, {y=}')

    def distancia(self, outro: 'Ponto'):
        dx = self.x - outro.x
        dy = self.y - outro.y
        d = math.sqrt(dx**2 + dy**2)
        return d

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
        
    def distancia_origem(self): 
        dx = self.x  - 0
        dy = self.y  - 0
        d = math.sqrt(dx**2 + dy**2)
        return d
    
    def iguais(self, outro: 'Ponto'):
        return self.x == outro.x and self.y == outro.y

print('Criando pontos')
p1 = Ponto(2, 3)
p2 = Ponto(2, 3)
p3 = Ponto(5, 4)

p1.exibir()
p3.exibir()

print(p1.distancia(p3))
print(p1.iguais(p2))
print(p1.iguais(p3))
print(p1.distancia_origem())




