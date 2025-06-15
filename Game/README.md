# Jogo da Forca (versão em Python)

Um jogo simples de **forca** feito em Python, onde o jogador deve adivinhar uma palavra aleatória com um número limitado de tentativas.

---

## Como funciona

* O jogo seleciona uma palavra aleatória a partir de um arquivo `palavras.txt`.
* O jogador tenta adivinhar a palavra letra por letra.
* A cada erro, uma chance é perdida.
* O jogo termina com vitória (ao descobrir a palavra) ou derrota (ao acabar as chances).

---

## Como executar

1. **Clone ou baixe** este repositório.
2. Certifique-se de que você tem **Python 3** instalado.
3. Crie um arquivo `palavras.txt` no mesmo diretório contendo uma palavra por linha. Exemplo:

```
caneta
lapis
borracha
caderno
livro
```

4. Execute o jogo no terminal:

```bash
python forca.py
```

---

## Estrutura do projeto

```
forca/
│
├── forca.py         # Arquivo principal do jogo
├── palavras.txt     # Lista de palavras utilizadas
└── README.md        # Este arquivo
```

---

## Funcionalidades

* Limpeza da tela a cada rodada (Windows, macOS, Linux)
* Entrada de letras validada (sem repetições ou entradas inválidas)
* Exibição de letras erradas e chances restantes
* Mensagem final indicando vitória ou derrota

---

## Melhorias futuras (ideias)

* Suporte a palavras com acento
* Adição de dicas para cada palavra
* Interface gráfica com Tkinter
* Contador de vitórias e derrotas
* Modo multiplayer

---

## Licença

Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e distribuir.

---
