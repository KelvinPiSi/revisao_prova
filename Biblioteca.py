from livros import l1, l2
from livrosDigitais import d1

class Biblioteca:
    def __init__(self):
        self.livros = []



    def registrar(self, livro: object) -> None:
        self.livros.append(livro)

    def contagem(self):
        for livro in self.livros:
            print(livro)
bib = Biblioteca()
bib.registrar(l1)
bib.registrar(l2)
bib.registrar(d1)
bib.contagem()