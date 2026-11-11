import math





class Ponto:
    # definicao das métodos
    def __init__(self, x, y):
        # definicao dos atributos
        self.x = x
        self.y = y

    def exibir(self):
        x = self.x
        y = self.y
        print(f'{x=}, {y=}')

    def distancia(self, outro: Ponto):
        dx = self.x - outro.x
        dy = self.y - outro.y
        d = math.sqrt(dx**2 + dy**2)
        return d

    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy

    def distancia_origem(self,): 


print('Criando pontos')
p = Ponto(2, 3)
a = Ponto(5, 4)

p.exibir() # exibir(p)
a.exibir()

print(p.distancia(a))

p.move(10, 20)
p.exibir()

