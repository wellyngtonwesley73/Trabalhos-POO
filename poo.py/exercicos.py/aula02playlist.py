class Playlist:
    def __init__ (self,nome,total_musicas,duracao):
        self.nome=nome
        self.total_musicas=total_musicas
        self.duracao=duracao

    def adicionar_musicas(self):    
        print('musica adicionada')

playlist = Playlist()

print()
#estatus pausado e tals metodos e atributos
