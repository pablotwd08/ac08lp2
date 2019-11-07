from abc import ABC, abstractmethod


class Cadastro:
    def __init__(self):
        self.pessoas = []

    def cadastrar_pessoa(self, pessoa):
        self.pessoas.append(pessoa)

    def exibir_cadastro(self):
        for i in self.pessoas:
            i.exibir_dados()


class Pessoa(ABC):
    def __init__(self, nome, nascimento):
        self.nome = nome
        self.nascimento = nascimento

    @abstractmethod
    def exibir_dados(self):
        pass


class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano


class Cliente(Pessoa):
    def __init__(self, nome, nascimento, codigo):
        super().__init__(nome, nascimento)
        self.codigo = codigo

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Nascimento: ", self.nascimento.dia, "/", self.nascimento.mes, "/", self.nascimento.ano)
        print("Codigo: ", self.codigo)


class Funcionario(Pessoa):
    def __init__(self, nome, nascimento, salario):
        super().__init__(nome, nascimento)
        self.salario = salario
        self.imposto = 0.05

    def calcular_imposto(self):
        return self.salario * self.imposto

    def exibir_dados(self):
        print("Nome: ", self.nome)
        print("Nascimento: ", self.nascimento.dia, "/", self.nascimento.mes, "/", self.nascimento.ano)
        print("Salario: ", self.salario)
        print("Imposto: ", self.salario * self.imposto)


class Gerente(Funcionario):
    def __init__(self, nome, nascimento, salario, setor):
        super().__init__(nome, nascimento, salario)
        self.setor = setor
        self.imposto = 0.07

    def calcular_imposto(self):
        return self.salario * self.imposto

    def exibir_dados(self):
        super().exibir_dados()
        print("Area: ", self.setor)


data1 = Data(18, 10, 2000)
data2 = Data(25, 10, 2000)
data1 = Data(18, 10, 2000)
cliente1 = Cliente("Paulo", data1, 111)
cliente2 = Cliente("Joao", data2, 222)
func = Funcionario("Ana", data2, 2000.0)
ger = Gerente("Maria", data2, 4000.0, "TI")


cad = Cadastro()
cad.cadastrar_pessoa(cliente1)
cad.cadastrar_pessoa(cliente2)
cad.cadastrar_pessoa(func)
cad.cadastrar_pessoa(ger)


cad.exibir_cadastro()
