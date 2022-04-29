from pessoa_banco import Pessoa

class Conta:
    contas_abertas= 0
    def __init__(self, objetosPessoa= [], saldo= 0, Nconta= 0):

        self.clientes= objetosPessoa
        self.saldo= saldo
        self.nomes= []
        self.cpf= []
        self.telefone= []
        self.email= []
        self.extrato= []
        self.numero_conta = Nconta
        Conta.contas_abertas+= 1


    def confirmaTitular(self, cpf):
        """Confirma se a solicitação veio realmente de algum dos titulares."""
        nome = ''
        if cpf in self.cpf:
            indice = self.cpf.index(cpf)
            nome = self.nomes[indice]
        else:
            nome= False

        return nome

    def getCliente(self):
        a= ''
        for i in self.clientes:
            a += i.getNome()
        return a

    def getNumeroConta(self):
        return self.numero_conta

    def getAtributos(self):
        """Método necessário para possibilitar contas com mais de um tirular."""

        a = ''
        for i in self.clientes:
            self.nomes.append(i.getNome())
            self.cpf.append(i.getCpf())
            self.telefone.append(i.getTelefone())
            self.email.append(i.getEmail())
        print("Atributos definidos com sucesso!")

    def historico(self, cliente, operacao= 0 , valor=  0):

        match operacao:
            case 0:
                self.extrato.append(f"Operação: Extrato realizado pelo(a): {cliente}")

            case 1:
                self.extrato.append(f"Depósito de R${valor}"+'\t'+ f"Titualr que realizou: {cliente}")

            case 2:
                self.extrato.append(f"Saque de R${valor}"+ "\t" + f'Titular que realizou: {cliente}')

            case 3:
                self.extrato.append(f"Depósito realizado pelo CPF de número: {cliente} no valor de: R${valor}")

        
    def getHistorico(self, cpf):
        """Retorno vazio. Printa o histórico para o cliente."""
        nome= Conta.confirmaTitular(self, cpf)
        if nome != False:
            Conta.historico(self, nome)
            for i in self.extrato:
                print(i)


    def getSaldo(self, cpf):
        """Retorna o saldo atual da conta."""
        a= Conta.confirmaTitular(self, cpf)
        if a != False:
            return self.saldo

    def deposito(self, cpf, valor):
        """Método que realiza a alteração no saldo da conta (permite depósito por outras pessoas nçao titulares)"""

        a= Conta.confirmaTitular(self, cpf)
        if a == False:
            Conta.historico(self, cpf, 3, valor)
            self.saldo += valor

        if a != False:
            Conta.historico(self, a, 1, valor)
            self.saldo+= valor

        print("Deposito realizado com sucesso!")

    def saque(self, cpf, valor):
        """Método que realiza saques"""

        a= Conta.confirmaTitular(self, cpf)
        if a != False:
            if valor < self.saldo:
                self.saldo -= valor
                Conta.historico(self, a, 2, valor)
                print("Saque realizado com sucesso.")
            else:
                print(f"saldo insuficiente."+ '\n'+ f'Saldo atual: R${Conta.getSaldo(self, cpf)}')
        else:
            print("Operação só pode ser realizada por um dos titulares.")

    def encerrarConta(self):
        self.clientes= ''
        self.saldo= 0
        self.nomes= []
        self.cpf= []
        self.telefone= []
        self.email= []
        self.extrato= []
        self.numero_conta = 0
        Conta.contas_abertas-= 1

    def __str__(self):
        return "\n"+f"Número da conta: {self.getNumeroConta()}" + '\n'+ f"Titulares: {self.getCliente()}"
