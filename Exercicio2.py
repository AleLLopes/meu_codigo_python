#2 - Faça um algoritmo para receber
# um número qualquer e imprimir na tela se o
# número é par ou ímpar, positivo ou negativo
num = int(input("Digite um número: "))
if num % 2 == 0:
    print("O número é PAR.")
else:
    print("O número é ÍMPAR.")
if num > 0:
    print("O número é POSITIVO.")
elif num < 0:
    print("O número é NEGATIVO.")
else:
    print("O número é ZERO.")