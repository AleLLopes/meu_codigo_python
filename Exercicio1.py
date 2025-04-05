#1 - Faça um algoritmo que leia os valores de A, B, C
# e em seguida imprima na tela a soma entre A e B é
# mostre se a soma é menor que C.
A = float(input("Digite o valor de A: "))
B = float(input("Digite o valor de B: "))
C = float(input("Digite o valor de C: "))
soma = A + B
print(f"A soma de A e B é: {soma}")
if soma < C:
    print("A soma de A e B é menor que C.")
else:
    print("A soma de A e B não é menor que C.")