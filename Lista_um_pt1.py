def question1A():
    """Função que recebe informações de artilheiros e retorna uma matriz com elas: -> [[],[]...]"""

    accumulator = 0
    matrix = []
    final_matrix = []

    while True:
        accumulator += 1

        match accumulator:

            case 1:

                b = str(input("Digite o nome do artilheiro: "))
                
                if b == 'fim':
                    break
                
                else:
                    matrix.append(b)

            case 2:

                b = str(input("Digite até qual rodada o mesmo atuou (Oitavas, Oitavas, Quartas, Semi, Final): "))
                matrix.append(b)

            case 3:
                
                b = int(input("Digite quantos gols o mesmo marcou: "))
                matrix.append(b)
                final_matrix.append(matrix)
                matrix = []
                accumulator = 0

    return final_matrix


def question1B(matrix):
    """Função que recebe uma matriz com informações do campeaonato e devolve uma matriz\
         com os artilheiros e a media de gols de cada: [[...],[...]...] -> [...]"""
    
    accumulator = 0
    final_matrix = []
    matches = 0
    
    for i in matrix:

        for j in i:
            accumulator += 1

            match accumulator:
                case 1:

                    final_matrix.append('Jogador: ')
                    final_matrix.append(j)

                case 2:

                    match j:
                        case "Classificatórias":
                            matches = 3 

                        case "Oitavas":
                            matches = 4

                        case "Quartas":
                            matches = 5

                        case "Semi":
                            matches = 6

                        case "Final":
                            matches = 7
                case 3:

                        final_matrix.append("Média de gols: ")
                        final_matrix.append((j / matches))
                        accumulator = 0

    return final_matrix

