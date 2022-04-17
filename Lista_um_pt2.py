# Aluno: Márcio Maia; Professor: Mitre Costa Dourado; Lista 1 - computação II

from random import sample as sp
from random import randint as rt


def question2(qtd_car):
    """Bingo!!! Dados os números de cartelas participante, as cria: int -> [[],[],...]"""

    matrix = []
    prize_draw= []
    card = []
    winner = False
    card_index = 0

    for i in range(1, 60):
        card.append(i)

    while len(matrix) != qtd_car:

        matrix.append(sp(card, 6))

    card = []

    while winner == False:
        b = rt(1,60)

        if b not in prize_draw:
            prize_draw.append(b)

        for i in matrix:
            i.sort()
            prize_draw.sort()
            hits = 0

            for j in i:
                
                if j in prize_draw:
                    hits += 1

                if hits == 6:
                    winner = True
                    card = i
                    card_index = matrix.index(card)

    
    return prize_draw, card, card_index


def main():
    b = int(input("Quantas cartelas participaram?"))
    a = question2(b)
    print(f"Números sorteados: {a[0]}")    
    print(f"Cartela vencedora: {a[1]}")
    print(f"Número da cartela: {a[2]}")

if __name__ == "__main__":
    main()
