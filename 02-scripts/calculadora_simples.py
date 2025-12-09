# Script: Calculadora Simples
# Recebe dois números e exibe as quatro operações básicas.

a = float(input("Primeiro número: "))
b = float(input("Segundo número: "))

print("Soma:", a + b)
print("Subtração:", a - b)
print("Multiplicação:", a * b)

if b != 0:
    print("Divisão:", a / b)
else:
    print("Divisão: impossível (divisão por zero)")
