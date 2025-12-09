# Script: Contador de Palavras
# Ele lê uma frase e depois conta quantas palavras essa frase possui.

frase = input("Digite uma frase: ")

palavras = frase.split()  # separa por espaços
quantidade = len(palavras)

print("Total de palavras:", quantidade)
