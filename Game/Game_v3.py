# Desenvolvimento de game em Python - Projeto do curso DSA
# Haangman 
# Programação orientada a objetos

import random
from os import system, name

def limpa_tela():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

board = ['''

>>>>>>>>>>Hangman<<<<<<<<<<

+---+
|   |
    |
    |
    |
    |
=========''', r'''

+---+
|   |
O   |
    |
    |
    |
=========''', r'''

+---+
|   |
O   |
|   |
    |
    |
=========''', r'''

 +---+
 |   |
 O   |
/|   |
     |
     |
=========''', r'''

 +---+
 |   |
 O   |
/|\  |
     |
     |
=========''', r'''

 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========''', r'''

 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========''']

class Hangman:
    def __init__(self, palavra):
        self.palavra = ''
        self.letras_tentadas = [] # lista vazia p/ guardar letras tentadas
        self.letras_certas = [] # lista vazia p/ guardar letras certas
        self.contador_erros = 0
        self.limite_erros = 6 # máximo de erros permitidos por rodada
        self.lista_palavras('palavras.txt')

    def lista_palavras(self, caminho_arquivo):
        with open(caminho_arquivo, 'r') as arquivo: # abre o arquivo em modo leitura
            palavras = [linha.strip() for linha in arquivo if linha.strip()]
        self.palavra = random.choice(palavras).lower()

    def jogo_finalizado(self):
        return self.contador_erros >= self.limite_erros
        # retorna True se o número de erros atingiu o limite
    
    def vencedor(self):
        for letra in self.palavra:
            if letra not in self.letras_certas:
                return False
        return True
    # verifica se as letras da palavra foram advinhas

    def mostra_palavra(self):
        resultado = ''
        for letra in self.palavra:
            if letra in self.letras_certas:
                resultado += letra + ' '
            else:
                resultado += '_ '
        return resultado.strip()
    # retorna uma string com as letras e _ no lugar das não advinhadas

    def mostrar_status(self):
        print(board[self.contador_erros])
        print("\nLetras já tentadas:", ' '.join(self.letras_tentadas))
        print("Progresso:", self.mostra_palavra())
    # mostra o board, as letras tentadas e o progresso da palavra
        
if __name__ == "__main__":
    jogo = Hangman('')  # a palavra será carregada do arquivo dentro do __init__

    while not jogo.jogo_finalizado() and not jogo.vencedor():
        jogo.mostrar_status()
        tentativa = input("\nDigite uma letra: ").lower()

        if not tentativa.isalpha() or len(tentativa) != 1:
            print("Digite apenas uma letra!")
            continue

        if tentativa in jogo.letras_tentadas:
            print("Você já tentou essa letra.")
            continue

        jogo.letras_tentadas.append(tentativa)

        if tentativa in jogo.palavra:
            jogo.letras_certas.append(tentativa)
            print("Boa! Letra correta.")
        else:
            jogo.contador_erros += 1
            print("Letra errada!")

    # Final do jogo
    jogo.mostrar_status()
    if jogo.vencedor():
        print("\nParabéns! Você venceu. A palavra era:", jogo.palavra)
    else:
        print("\nVocê perdeu. A palavra era:", jogo.palavra)
