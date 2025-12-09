# Script: Gerador de Senha Simples
# Cria uma senha aleatória composta por letras e números.

import random
import string

tamanho = 10  # tamanho da senha

caracteres = string.ascii_letters + string.digits
senha = "".join(random.choice(caracteres) for _ in range(tamanho))

print("Senha gerada:", senha)
