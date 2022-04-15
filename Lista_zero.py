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
    print(b)
    print(bigger)
    if bigger == False:
        c = b[-mult:]
        for i in c:
            summation *= i

        return summation, f'Matriz: {b}'

    if accumulator == True:
        string = f"Somatório: {sum(b)}\nmatriz: {b}"
        return string

        
def question2():
    """Função que quando passada """