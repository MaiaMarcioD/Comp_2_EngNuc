
class Pessoa:

    def __init__(self, nome, m=0, n=0, cpf= 0, telefone = 0):
        self.posicao= [int(m),int(n)]
        self.nome= nome
        self.cpf= cpf
        self.telefone= telefone


    def adTelefone(self, telefone):
        self.telefone = telefone   
        a= f"O número {self.telefone} adicionado ao perfil do: {self.nome}"
        return a

    def adCpf(self, cpf):
        self.cpf = cpf 
        a= f"O CPF {cpf} adicionado ao perfil do: {self.nome} "
        return a

    def alteraPos(self, linha, coluna):
        self.posicao = [int(linha), int(coluna)]
        a= f"A posição do(a) {self.nome}, foi alterada para: {linha}{coluna}"
        return a

    def __str__(self):
        print(self.nome)
