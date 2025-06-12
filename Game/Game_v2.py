# Desenvolvimento de game em Python - Projeto do curso DSA

import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def game():
    limpa_tela()
    print("\nBem-vinde ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")

    # Lê as palavras do arquivo
    try:
        with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
            palavras = [linha.strip().lower() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print("Erro: Arquivo 'palavras.txt' não encontrado.")
        return

    if not palavras:
        print("Erro: Nenhuma palavra encontrada no arquivo.")
        return

    palavra = random.choice(palavras)
    letras_descobertas = ['_' for _ in palavra]
    chances = 8
    letras_erradas = []

    while chances > 0:
        print(" ".join(letras_descobertas))
        print("\nChances restantes:", chances)
        print("Letras erradas:", " ".join(letras_erradas))

        tentativa = input("\nDigite uma letra: ").lower()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("\nDigite apenas UMA letra válida.")
            continue

        if tentativa in letras_descobertas or tentativa in letras_erradas:
            print("\nVocê já tentou essa letra. Tente outra.")
            continue

        if tentativa in palavra:
            for index, letra in enumerate(palavra):
                if letra == tentativa:
                    letras_descobertas[index] = letra
        else:
            chances -= 1
            letras_erradas.append(tentativa)

        if "_" not in letras_descobertas:
            print("\nParabéns! Você venceu!")
            print("A palavra era:", palavra)
            break

    if "_" in letras_descobertas:
        print("\nVocê perdeu. A palavra era:", palavra)

# bloco main
if __name__ == "__main__":
    game()
