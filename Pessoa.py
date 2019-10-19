class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def setNome(self, nome):
        self.nome = nome

    def setIdade(self, idade):
        self.idade = idade

    def setCPF(self, cpf):
        self.cpf = cpf

    def getNome(self):
        return self.nome

    def getIdade(self):
        return self.idade

    def getCPF(self):
        return self.cpf
