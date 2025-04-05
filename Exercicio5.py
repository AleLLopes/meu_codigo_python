#5 - Faça um algoritmo que leia o valor do salário mínimo e o valor
# do salário de um usuário, calcule quantos salários mínimos
salario_minimo = float(input("Digite o valor do salário mínimo: "))
salario_usuario = float(input("Digite o valor do seu salário: "))
quantidade = salario_usuario / salario_minimo
print(f"Você recebe {quantidade:.2f} salários mínimos.")