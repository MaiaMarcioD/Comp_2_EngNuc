from random import randint as rt

def question1(matriz = [], posição = 25, numero = 100, mult = 25, tamanho = 50):
    """Função que dada uma matriz mxn numérica (caso não seja passada nenhuma matriz, será criada de forma aleatória),
     x posição para interpretar, caso os x primeiros numeros sejam inferiores a k, os y's últimos números serão multiplicados.
     Caso contrário, retorna o somátorio de todos os números"""

    accumulator = 0
    summation = 1
    b = matriz
    bigger = False

    
    if matriz == []:

        while True:
            
            b.append(rt(-1000, 1000))
            accumulator+=1

            if accumulator == tamanho:
                accumulator = 0

                break

    for i in range(len(b)):
        accumulator += 1

        if b[i] > numero and accumulator < posição:
            bigger = True

            break
    
    if bigger == False:
        c = b[-mult:]
        
        for i in c:
            summation *= i

        return summation, f'Matriz: {b}'

    if bigger == True:
        string = f"Somatório: {sum(b)}"+'\n'+f"matriz: {b}"

        return string

        
def question2(sequencia = [], tamanho_seq = 15, posição = 14, parametro_1 = 100, parametro_2 = 200): 
    # A partir de uma série aleatória de 10 ou mais números, pode ser que demore a devolver a resposta.
    """Função que quando passada uma posição x, e os números que x tem que estar entre. 
    Retorna a sequência crescente (gerada aleatoriamente) com todas as exigencias expecificadas. """

    sequence = sequencia
    crescent = True
    accumulator = -1
    stopwatch = 0

    if sequence == []:

        while True:

            sequence.append(rt(-1000, 1000)) # Atualização não feita: Possibilitar que o usuário escolha o domínio do sorteio (fácil).
            accumulator += 1

            if len(sequence) >= 2:            
                if sequence[accumulator-1] < sequence[-1]:
                    crescent = True

                if sequence[accumulator-1] > sequence[-1]:
                    crescent = False
                    sequence = []
                    accumulator = -1

            if len(sequence) == posição:
                if parametro_1 < sequence[-1] and sequence[-1] < parametro_2:
                        
                    continue

                if parametro_1 > sequence[-1] or sequence[-1] > parametro_2:
                    sequence = []
                    accumulator = -1

            if len(sequence) == tamanho_seq and crescent == True:

                return f"Sequência: {sequence}"

    if sequence != []:

        for i in range(len(sequence)):

            if i > 0:
                if sequence[i] > sequence[i-1]:
                    crescent = True

                if sequence[i] < sequence[i-1]:
                    crescent = False

                    return f"Esta sequencia -{sequence}- não preencheu todos os requisitos, pois: Crescente = {crescent} "

        if sequence[posição -1] > parametro_1 and sequence[posição -1] < parametro_2:

            return f"Esta sequencia -{sequence}- preencheu todos os requisitos"

        else:

            return f"Esta sequencia -{sequence}- não preencheu todos os requisitos, pois: o número de posição {posição},\
                 não está entre os parâmetros "
            
