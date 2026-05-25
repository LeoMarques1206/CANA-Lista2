import random

def maior1(vetor):
    pos = 0
    while vetor[pos + 1] > vetor[pos]:
        pos = pos + 1
    return vetor[pos]


def maior2(vetor, i, f):

    if i == f:
        return vetor[i]

    m = (i + f) // 2

    if vetor[m] < vetor[m + 1]:
        return maior2(vetor, m + 1, f)
    else:
        return maior2(vetor, i, m)


def criaVetorUnimodal(n):
    vetor = [0 for x in range(n)]

    vetor[0] = random.randint(0, 9)
    for i in range(1, n):
        vetor[i] = vetor[i - 1] + random.randint(0, 9) + 1

    a = random.randint(1, n - 2)
    b = n - 1

    while a < b:
        vetor[a], vetor[b] = vetor[b], vetor[a]
        a += 1
        b -= 1

    return vetor

A = criaVetorUnimodal(12)

print("Vetor unimodal:")
print(A)

m1 = maior1(A)
print("Maior pelo método iterativo:", m1)

m2 = maior2(A, 0, len(A) - 1)
print("Maior pelo método recursivo:", m2)


"""
Análise da recorrência:

Seja T(n) o tempo de execução da função maior2 para um subvetor com n elementos

- Caso base:
Quando i == f, resta apenas um elemento e a função retorna em tempo constante
T(1) = Θ(1)

- Passo recursivo:
Em cada chamada, o algoritmo:
1. Calcula o índice do meio
2. Compara vetor[m] com vetor[m + 1]
3. Faz apenas uma chamada recursiva para metade do vetor

O trabalho realizado fora da recursão é constante: Θ(1)
O tamanho do subproblema é reduzido para n/2

Portanto, a equação de recorrência é:

T(n) = T(n/2) + Θ(1)

Resolvendo a recorrência:

n -> n/2 -> n/4 -> n/8 -> ... -> 1

O número de divisões por 2 até chegar a 1 é log2(n)

Logo:

T(n) = Θ(log n)

Portanto, a complexidade do algoritmo é O(log n) 

"""