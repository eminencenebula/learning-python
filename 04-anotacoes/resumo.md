📝 Resumo de Estudos – Python

Este arquivo reúne anotações rápidas sobre os principais conceitos que estou aprendendo em Python.  
As explicações são simples e diretas, focadas em entender "o porquê" das coisas.

...

📌 Variáveis
São espaços na memória que guardam valores.

Exemplos:

nome = "Lexa"
idade = 22
altura = 1.70


📌 Tipos de dados básicos

int — números inteiros
float — números decimais
str — textos (strings)
bool — True / False
list — lista mutável
tuple — tupla imutável
dict — dicionário (chave: valor)


📌 Entrada e saída

input("Digite algo: ")
print("Texto")


📌 Condicionais

Permitem que o programa tome decisões.

if condição:
    bloco
elif outra_condição:
    bloco
else:
    bloco


📌 Loops
for

Usado para repetir algo um número conhecido de vezes.

for i in range(5):
    print(i)

while

Repete enquanto a condição for verdadeira.

while x > 0:
    x -= 1


📌 Funções

Organizam o código e evitam repetição.

def saudacao(nome):
    return "Olá, " + nome



📌 Listas
Coleções ordenadas e mutáveis.

Copiar código
numeros = [4, 7, 1]
numeros.append(10)



📌 Dicionários

Guarda dados em pares chave:valor.

pessoa = {"nome": "Lexa", "idade": 22}


📌 Erros comuns

Esquecer os dois pontos :

Errar identação

Confundir string com número

Loop infinito com while True sem break
