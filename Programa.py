class Programa:
    pass
    def __init__(self, nome, ano): #Metodo Construtor
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes
    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, Novo_nome):
        self._nome = Novo_nome.title()

    def __str__(self):
        return f'{self._nome} / {self.ano} / {self._likes} likes'