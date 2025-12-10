# Desafio: Criar uma função que diz se um número é primo.

def eh_primo(n):
    if n < 2:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):  # apenas até a raiz quadrada
        if n % i == 0:
            return False
    
    return True

# Testes
print("7 é primo?", eh_primo(7))
print("10 é primo?", eh_primo(10))
print("13 é primo?", eh_primo(13))
