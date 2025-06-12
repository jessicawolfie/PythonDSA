# Desenvolvimento de game em Python - Projeto do curso DSA

import random
from os import system, name

# função para limpar a tela
def limpa_tela():

    # windows
    if name == 'nt':
        _ = system('cls')

    # mac ou linux
    else:
        _ = system('clear')

def game():

    limpa_tela()
    print("\nBem-vinde ao jogo da forca!")
    print("Advinhe a palavra abaixo:\n")

    # lista de palavras para o jogo
    palavras = ['caneta', 'lapis', 'borracha', 'caderno', 'livro']

    # escolhe uma palavra randomicamente
    palavra = random.choice(palavras)

    letras_descobertas = [ '_' for letra in palavra]

    chances = 8 # tomar cuidado com a escolha da palavra, pois se a mesma tiver 8 letras, não dará tempo do usuário escolher as letras.

    letras_erradas = [] # lista vazia para receber as letras erradas


    # loop enquanto  número de chances for maior do que zero
    while chances > 0:
        print(" ".join(letras_descobertas)) # join faz a junção do que está de ambos os lados
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if tentativa in palavra:
            index = 0

            for letra in palavra:
                if tentativa == letra:
                    letras_descobertas[index] = letra
                index += 1
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nVocê venceu! A palavra era:", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu. A palavra era", palavra)

# bloco main
if __name__ == "__main__":
    game()