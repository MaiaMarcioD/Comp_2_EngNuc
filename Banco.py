from Conta import Conta
from pessoa_banco import Pessoa

class Banco:

    def __init__(self, nome, contas= [], clientes= []):

        self.nome_banco= nome
        self.contas= contas
        self.clientes= clientes

    def cadastrasCliente(self):
        """Método usado para cadastrar novos clientes."""
        nome= str(input("Nome cliente: "))
        cpf= int(input("Cpf do cliente: "))
        telefone= int(input("Telefone do cliente: "))
        email= str(input("Email do cliente: "))
    
        return self.clientes.append(Pessoa(nome, cpf, telefone, email))



    def criaContas(self, saldo= 0, numeroC= 0):
        titulares = []
        quantidade= int(input("Quantos titulares?"))
        contador = 0
        while contador < quantidade:
            Banco.cadastrasCliente(self)
            contador += 1 
        for i in self.clientes[-quantidade:]:
            titulares.append(i)

        self.contas.append(Conta(titulares))
        self.contas[-1].getAtributos()

        print("Conta aberta com sucesso.")

    def mostraContas(self):
        for i in self.contas:
            print(i)

    def mostraClientes(self):
        for i in self.clientes:
            print(i)
