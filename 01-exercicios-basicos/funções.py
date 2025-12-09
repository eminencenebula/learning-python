# Exercícios de funções

# 1. Função de saudação
def saudacao(nome):
    return f"Olá, {nome}!"

print(saudacao("Lexa"))

# 2. Função para somar dois números
def soma(a, b):
    return a + b

print("Soma:", soma(5, 3))

# 3. Função que retorna se um número é par
def eh_par(num):
    return num % 2 == 0

print("É par?", eh_par(8))
print("É par?", eh_par(5))

# 4. Função para calcular o quadrado de um número
def quadrado(n):
    return n ** 2

print("Quadrado:", quadrado(7))
