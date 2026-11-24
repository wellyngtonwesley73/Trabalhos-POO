class Playlist:
    def __init__(self):
        # Atributos de instância
        self.nome = ""
        self.criador = ""
        self.total_musicas = 0
        self.duracao_total_minutos = 0.0
        self.publica = False

    def adicionar_musica(self, duracao):
        self.total_musicas += 1
        self.duracao_total_minutos += duracao

    def remover_musica(self, duracao):
        if self.total_musicas > 0:
            self.total_musicas -= 1
        self.duracao_total_minutos = max(0.0, self.duracao_total_minutos - duracao)

    def tornar_publica(self):
        self.publica = True

    def tornar_privada(self):
        self.publica = False

    def exibir_estado(self):
        visibilidade = "Pública" if self.publica else "Privada"
        return (
            f"Playlist: {self.nome} | Criador: {self.criador} | "
            f"Músicas: {self.total_musicas} | Duração: {self.duracao_total_minutos:.1f} min | "
            f"Status: {visibilidade}"
        )


# Instanciação e testes do objeto
p1 = Playlist()
p1.nome = "Indie Rock Favoritas"
p1.criador = "Wesley"

p1.adicionar_musica(3.5)
p1.adicionar_musica(4.2)
p1.tornar_publica()

print(p1.exibir_estado())

p1.remover_musica(3.5)
p1.tornar_privada()

print(p1.exibir_estado())
#estatus pausado e tals metodos e atributos
