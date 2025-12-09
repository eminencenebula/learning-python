# Exercícios de condicionais

# 1. Verificar se um número é positivo
numero = int(input("Digite um número: "))
if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
else:
    print("Zero")

# 2. Verificar se é maior de idade
idade = int(input("Digite sua idade: "))
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")

# 3. Checar senha simples
senha = input("Digite a senha: ")
if senha == "python123":
    print("Acesso permitido")
else:
    print("Senha incorreta")
