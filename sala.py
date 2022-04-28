from pessoa import Pessoa

class Sala:
    def __init__(self, m, n):
        self.linhas= m
        self.colunas= n
        self.array= []
        self.space= []
        self.livre= True
        self.pessoas= []

    def criaArray(self):

        for i in range(self.linhas):
            self.array = []
            for j in range(self.colunas):
                
                if i == 0 or i == self.linhas - 1 or j == 0 or j == self.colunas -1:
                    self.livre = False
                    self.array.append(self.livre)

                if i != 0 and i != self.linhas - 1 and j !=  0 and j != self.colunas - 1:
                    self.livre = True
                    self.array.append(self.livre)

            self.space.append(self.array)

    def criaPessoa(self, nome):
        self.pessoas.append(Pessoa(nome))

    def alocarPessoa(self, nome, m, n):
        indice = 0
        for objetoPessoa in self.pessoas:
            if objetoPessoa.nome == nome:
                break
            indice += 1

        linha= m -1
        coluna= n -1 
        objetoPessoa.alteraPos(linha, coluna)
        if self.space[linha][coluna] == True:

            self.space[linha][coluna] = [objetoPessoa.nome, objetoPessoa.cpf]
            a= f"A pessoa com o nome de {objetoPessoa.nome}, de cpf: {objetoPessoa.cpf} foi alocada na posição desejada."

        if self.space[linha][coluna] != True:
            if self.space[linha][coluna] == False:
                b= "parede"
            if self.space[linha][coluna] != False:
                b= "pessoa"

            a= f"Por favor, aloque o(a) {objetoPessoa.nome} de cpf: {objetoPessoa.cpf} em outra posição, pois no lugar desejado há uma {b}."

        return a
    
    def pessoaParede(self, coluna, linha, direcao):
        b= ''
        L= 0
        C= 0
        match direcao:
            case direcao if direcao == "cima":
                L= -1   
                C= 0
            case direcao if direcao == "baixo":
                L= 1
                C= 0
            case direcao if direcao == "esquerda":
                L= 0
                C= -1
            case direcao if direcao == "direita":
                L= 0
                C= 1
        if self.space[linha+L][coluna+C] == False:
            b= "Há uma parede no local escolhido."

        if self.space[linha+L][coluna+C] != False:
            b= "Há uma pessoa no local escolhido"

        return print(b)
    
    def alteraArray(self,indice, direcao):
        linha= self.pessoas[indice].posicao[0]
        coluna= self.pessoas[indice].posicao[1]
        nome= self.pessoas[indice].nome
        cpf= self.pessoas[indice].cpf
        a= ''
    
        match direcao:
            
            case direcao if direcao == "cima":
                if self.space[linha -1][coluna] == True:
                    self.space[linha -1][coluna] = [nome, cpf]
                    self.space[linha][coluna] = True
                    a= self.pessoas[indice].alteraPos(linha-1, coluna)

            case direcao if direcao == "baixo":
                if self.space[linha+1][coluna] == True:
                    self.space[linha +1][coluna] = self.pessoas[indice].nome
                    self.space[linha][coluna] = True
                    a= self.pessoas[indice].alteraPos(linha+1, coluna)
                
            case direcao if direcao == "direita":
                if self.space[linha][coluna +1] == True:
                    self.space[linha][coluna +1] = [nome, cpf]
                    self.space[linha][coluna] = True
                    a= self.pessoas[indice].alteraPos(linha, coluna+1)

            case direcao if direcao == "esquerda":
                if self.space[linha][coluna -1] == True:
                    self.space[linha][coluna -1] = [nome, cpf]
                    self.space[linha][coluna] = True
                    a= self.pessoas[indice].alteraPos(linha, coluna-1)

            case direcao if a == '':
                a= Sala.pessoaParede(self, linha, coluna, direcao)

        return print(a)

                

    def movimentar(self, nome, direcao):
        """Metodo que possibilita que o usuário escolha a direção desejada"""
        indice = 0
        for i in self.pessoas:
            if i.nome == nome:
                Sala.alteraArray(self, indice, direcao)

            indice += 1

    

    def __str__(self):
        """Método que retorna uma imagem da sala no momento atual"""
        a = ''
        indice = 0
        for linhas in self.space:

            for colunas in linhas:
                if colunas == False and indice ==0 or indice == self.linhas -1:
                    a+= "||" + "\n" + "||"
                if colunas == True:
                    a += "    "
                if type(colunas) == Pessoa:
                    a+= colunas.nome
            indice +=1


        return a
