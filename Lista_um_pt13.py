# Aluno: Márcio Maia; Professor: Mitre Costa Dourado; Lista 1 - computação II

from random import shuffle as sf
from time import sleep


def question3(size= 4):
    """Função que especificada, ou não, o tamanho de uma matriz quadrática, executa um jogo da memória com o mesmo."""

    matrix = []
    memory = []
    hidden = []
    hidden_memory = []
    accumulator = 0
    accumulator1 = 0
    open_a = True
    open_b = True

    for element in range(1,((size*size) //2)+1):
        matrix.append(element)
        matrix.append(element)
        hidden.append("*")
        hidden.append("*")
        sf(matrix)

    for lines in range(size):
        accumulator += 1
        memory.append(matrix[((accumulator-1)*size): accumulator*size])
        hidden_memory.append(hidden[((accumulator-1)*size): accumulator*size])

    accumulator = 0
    
    for i in range(size):
                print(hidden_memory[i])
    while True:

        a = list(input(f"Escolha a linha desejada e a coluna deseja de: 1 a {size} "+ "\n"))
        b = list(input(f"Escolha a linha desejada e a coluna deseja de: 1 a {size}"+ "\n"))

        if len(a) > 3: # Para matrizes de ordem superior ou igual a 10
            for i in a:
                if i == " ":
                    break
                accumulator1 += 1
            a = "".join(a)
            a = [a[0:accumulator1]," ", a[accumulator1:]]
            accumulator1 = 0

        if len(b) > 3: # Para matrizes de ordem superior ou igual a 10
            for i in b:
                if i == " ":
                    break
                accumulator1 += 1
            b = "".join(b)
            b = [b[0:accumulator1]," ", b[accumulator1:]]
            accumulator1 = 0

        if a != b and int(a[0]) <= size and int(a[2]) <= size and int(b[0]) <= size and int(b[2]) <= size:

            if memory[int(a[0])-1][int(a[2])-1] == memory[int(b[0])-1][int(b[2])-1]:
                hidden_memory[int(a[0])-1][int(a[2])-1] = memory[int(a[0])-1][int(a[2])-1]
                hidden_memory[int(b[0])-1][int(b[2])-1] = memory[int(b[0])-1][int(b[2])-1]
                accumulator += 1
                print("\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n")
                if hidden_memory == memory:
    
                    break

                for i in hidden_memory:
                    print(i)
                    
            if memory[int(a[0])-1][int(a[2])-1] != memory[int(b[0])-1][int(b[2])-1]:

                if hidden_memory[int(b[0])-1][int(b[2])-1] == '*':
                    open_b = False

                if hidden_memory[int(a[0])-1][int(a[2])-1] == '*':
                    open_a = False

                hidden_memory[int(a[0])-1][int(a[2])-1] = memory[int(a[0])-1][int(a[2])-1]
                hidden_memory[int(b[0])-1][int(b[2])-1] = memory[int(b[0])-1][int(b[2])-1]

                for i in hidden_memory:
                    print(i)

                print(f"As coordenadas {a[0]}x{a[2]} e {b[0]}x{b[2]} não formam par")
                if open_b == False:
                    hidden_memory[int(b[0])-1][int(b[2])-1] = '*'
                
                if open_a == False:
                    hidden_memory[int(a[0])-1][int(a[2])-1] = '*'

                open_a = True
                open_b = True

                sleep(2)
                print("\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n"+"\n")

                for i in hidden_memory:
                    print(i)

                sleep(2)

        if a == b and int(a[0]) <= size and int(a[2]) <= size and int(b[0]) <= size and int(b[2]) <= size:
            print('Por favor, escolha pares diferentes.')

        if int(a[0]) > size or int(a[2]) > size or int(b[0]) > size or int(b[2]) > size: 
            print(f"Tais opções execederam o limite do jogo, por favor, tente entre a ordem desejada;\
                 Pode escolher de 1 a {size}")

        

    return hidden_memory, accumulator



def main():
    b = int(input("Escolha a ordem da matriz quadratica. (Ordem par)" + "\n"))
    a = question3(b)

    for i in a[0]:
        print(i)
    print(f"Número de tentativas: {a[1]}")

if __name__ == "__main__":
    main()