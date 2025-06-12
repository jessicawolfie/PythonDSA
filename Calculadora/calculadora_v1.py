print("\n******************* Calculadora em Python *******************\n")

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

while True:
    print("\n1 - soma\n2 - subtração\n3 - multiplicação\n4 - divisão\n")

    operacao = input("Selecione o número da operação que deseja realizar (1/2/3/4): ")

    if operacao not in ("1", "2", "3", "4"):
        print("Opção inválida. Tente novamente.")
        continue

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if operacao == "4" and num2 == 0:
        print("Erro: divisão por zero não é permitida.")
        continue

    if operacao == "1":
        resultado = soma(num1, num2)
    elif operacao == "2":
        resultado = subtracao(num1, num2)
    elif operacao == "3":
        resultado = multiplicacao(num1, num2)
    elif operacao == "4":
        resultado = divisao(num1, num2)

    print("Resultado:", resultado)

    continuar = input("Deseja fazer outra operação? (s/n): ").lower()
    if continuar != "s":
        print("Encerrando a calculadora. Até logo!")
        break
