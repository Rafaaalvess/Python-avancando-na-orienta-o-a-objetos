from Programa import Programa
class serie(Programa):#Entre parenteses a classe mãe
    pass
    def __init__(self, nome, ano, temporada):#Metodo Construtor
        super().__init__(nome,ano) #Gera a super classe para trazer parametros da classe mãe
        self.temporada = temporada

    def __str__(self):#Metodo sobreposto da classe mãe para usar parametros diferentes do que em outra classe
        return f'{self._nome} / {self.ano}/ {self.temporada} temporadas / {self._likes} likes'

