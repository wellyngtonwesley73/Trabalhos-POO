import math

# Definição das funções que manipulam
# as variáveis/dados
def exibir_ponto(x, y):
    print(f'{x=}, {y=}')

def distancia(x, y, x1, y1):
    dx = x-x1
    dy = y-y1
    d = math.sqrt(dx**2 + dy**2)
    return d

def move(x, y, dx, dy):
    x = x + dx
    y = y + dy
    return x, y

# Definicao das variáveis/dados
a = 2, 3
b = 5, 4
c = -2, 1

# Uso das funções com as variáveis
print('Usando função')
exibir_ponto(a[0], a[1])
exibir_ponto(b[0], b[1])

d = distancia(c[0], c[1], a[0], a[1])
print(f'{d=}')

a = move(a[0], a[1], 10, 20)
exibir_ponto(a[0], a[1]) # 12, 23




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
    

print('Criando pontos')
p = Ponto(2, 3)
a = Ponto(5, 4)

p.exibir() # exibir(p)
a.exibir()

print(p.distancia(a))

p.move(10, 20)
p.exibir()