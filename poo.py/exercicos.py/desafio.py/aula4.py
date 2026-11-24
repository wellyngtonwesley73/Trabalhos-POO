# Declaração de Classe
class Gafanhoto:
    def __init__(self): # Método Construtor
        # Atributos de Instância
        self.nome = ""
        self.idade = 0
        self.instrumento = ""

    # Métodos de Instância
    def aniversario(self):
        self.idade = self.idade + 1

    def mensagem(self):
        if self.instrumento:
            return (
                f"{self.nome} é Gafanhoto(a), tem {self.idade} anos de idade "
                f"e toca {self.instrumento}."
            )
        return f"{self.nome} é Gafanhoto(a) e tem {self.idade} anos de idade."


# Declaração de Objetos (exemplos da aula)
g1 = Gafanhoto()
g1.nome = "Maria"
g1.idade = 17
g1.aniversario()
print(g1.mensagem())

g2 = Gafanhoto()
g2.nome = "Mauro"
g2.idade = 53
print(g2.mensagem())

g3 = Gafanhoto()
print(g3.mensagem())

# Objeto com características pessoais
g4 = Gafanhoto()
g4.nome = "Wesley"
g4.idade = 18
g4.instrumento = "clarineta e clarone"
print(g4.mensagem())