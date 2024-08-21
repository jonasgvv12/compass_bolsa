class Pessoa:
    def __init__(self, id):
        self.id = id
        self.__nome = None

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor


pessoa = Pessoa(1)
pessoa.nome = "Jonas"

print(pessoa.nome)

print(pessoa.id)  