# Exercícios de loops

# 1. Mostrar números de 1 a 5
for i in range(1, 6):
    print("Número:", i)

# 2. Contagem regressiva
contador = 5
while contador > 0:
    print("Contagem:", contador)
    contador -= 1

# 3. Somar números de 1 a 10
soma = 0
for n in range(1, 11):
    soma += n
print("Soma de 1 a 10:", soma)

# 4. Loop para pedir nome até escrever 'sair'
while True:
    nome = input("Digite um nome (ou 'sair'): ")
    if nome == "sair":
        break
    print("Olá,", nome)
