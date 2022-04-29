class Pessoa:
    pessoas_cadastradas = 0

    def __init__(self, nome, cpf= 0, telefone= 0, email= ""):
        self.nome= nome
        self.cpf= cpf
        self.telefone= telefone
        self.email= email
        Pessoa.pessoas_cadastradas += 1

    def getNome(self):
        """Retorna o nome de forma indireta."""
        
        a= self.nome

        return a

    def getCpf(self):
        """Retorna o cpf de forma indireta."""
        a= self.cpf

        if self.cpf == 0:
            a= "Cpf ainda não cadastrado."

        return a

    def getTelefone(self):
        """Retorna o telefone de forma indireta."""
        
        a= self.telefone

        if self.telefone== 0:
            a= """Telefone ainda não cadastrado."""

        return a

    def getEmail(self):
        """Retorna o email de forma indireta."""

        a= self.email

        if self.email == "":
            a = "Email não cadastrado."

        return a

    def setNome(self, nome):
        """Caso o cliente queira alterar para um nome social."""

        self.nome= nome   
        a= "Nome alterado com sucesso!"

        return a    

    def setCpf(self, cpf):
        """Para alterar ou definir o cpf do cliente."""

        self.cpf= cpf   
        a= """Cpf salvo com sucesso!"""
        
        return a
    
    def set_telefone(self, telefone):
        """Para alterar, ou alocar o telefone do cliente."""

        self.telefone= telefone
        a= "Telefone salvo com sucesso!"

        return a

    def setEmail(self, email):
        """Para cadastrar, ou alterar o email do cliente."""

        self.email= email
        a= """Email alterado com sucesso!"""

        return a

    def __str__(self):
        """Para printar o objeto da classe."""

        return f"Nome: {self.getNome()}" + "\n" + f"CPF: {self.getCpf()}" + '\n' + f'Tefefone: {self.getTelefone()}' + '\n' + f'Email: {self.getEmail()}'+ '\n'
