from livros import Livros
class livrosDigitais(Livros):
    def __init__(self,titulo,autor,genero,ano, paginas, tamanho_mb):
        super().__init__(titulo,autor,genero, ano, paginas)
        self.__tamanho_mb = tamanho_mb
    def temp_leitura(self):
        print (f"Total de minutos lido: {self.paginas * 1.5}")

d1 = livrosDigitais("Torre do Alvorecer", "Sarah J.", "Romance", 2014, 614, tamanho_mb=34)

print(d1)

d1.temp_leitura()
