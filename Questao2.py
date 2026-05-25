import random
import string


class Crianca:
    def __init__(self):
        self.nome = ''
        for i in range(0, 10):
            self.nome = self.nome + random.choice(string.ascii_uppercase)

        self.idade = random.randint(6, 16)
        self.turno = 'M' if random.randint(0, 1) == 0 else 'T'


def imprime(lista):
    for c in lista:
        print(c.nome, c.idade, c.turno, sep='\t')
    print()


def organizaTurno(lista):
    p = 0 # O(1)
    r = len(lista) - 1 # O(1)

    x = 'M' # O(1)
    i = p - 1 # O(1)

    for j in range(p, r): # O(n)
        if lista[j].turno == x: # o(1)
            i += 1 # O(1)
            lista[i], lista[j] = lista[j], lista[i] # O(1)

    lista[i + 1], lista[r] = lista[r], lista[i + 1] # O(1)

    return lista # o(1)


def faixaEtaria(idade):
    if idade <= 10:
        return 0
    elif idade <= 14:
        return 1
    else:
        return 2


def organizaIdade(lista):
    grupo1 = [] # O(1) 
    grupo2 = [] # O(1) 
    grupo3 = [] # O(1) 

    for crianca in lista: # O(n)
        if crianca.idade <= 10: # O(1)
            grupo1.append(crianca) # O(1)
        elif crianca.idade <= 14: # o(1)
            grupo2.append(crianca) # O(1)
        else:                              
            grupo3.append(crianca) # O(1)

    k = 0 # O(1)

    for crianca in grupo1: # o(n1)
        lista[k] = crianca # O(1)
        k += 1 # O(1)

    for crianca in grupo2: # O(n2)
        lista[k] = crianca  # O(1)
        k += 1  # O(1)

    for crianca in grupo3: # O(n3)
        lista[k] = crianca  # O(1)
        k += 1  # O(1)

    return lista # O(1)


n = 20
criancas = []

for i in range(1, 21):
    criancas.append(Crianca())

print("Lista original:")
imprime(criancas)

organizaTurno(criancas)
print("Após organizar por turno:")
imprime(criancas)

organizaIdade(criancas)
print("Após organizar por faixa etária:")
imprime(criancas)


"""
Passo 2

Complexidade:
- O laço percorre o vetor apenas uma vez
- Cada iteração realiza apenas operações O(1)
- Tempo de execução total: O(n)

(linha por linha comentado ao lado da função)

Saída: 

Após organizar por turno:
UEHSIKVTPU      8       M
BENQSRPFFT      6       M
USUIRJFWND      16      M
ZAQMJRKLVS      16      M
SASTXDFCXR      12      M
UNRLPIDQDS      13      M
DZTLLKYXJM      9       M
PEQQROIUUS      16      M
WOJMYKEJLW      12      M
UVTTESSMLW      10      M
WHHAESNPYP      14      M
DARROZLVZU      12      M
KLDGSBPYRZ      6       T
DXSKDOWEUH      11      T
MBCAOPOMOL      7       T
CGJDOEOTSZ      7       T
AJCXFXWYUV      6       T
RWOJIIJGOB      13      T
SEGYVFEPBF      11      T
IYHXKWYPIU      12      T


Passo 3

Complexidade:
- Cada elemento é analisado no máximo uma vez
- Tempo de execução: O(n)

(linha por linha comentado ao lado da função)

Saída: 

Após organizar por faixa etária:
UEHSIKVTPU      8       M
BENQSRPFFT      6       M
DZTLLKYXJM      9       M
UVTTESSMLW      10      M
KLDGSBPYRZ      6       T
MBCAOPOMOL      7       T
CGJDOEOTSZ      7       T
AJCXFXWYUV      6       T
SASTXDFCXR      12      M
UNRLPIDQDS      13      M
WOJMYKEJLW      12      M
WHHAESNPYP      14      M
DARROZLVZU      12      M
DXSKDOWEUH      11      T
RWOJIIJGOB      13      T
SEGYVFEPBF      11      T
IYHXKWYPIU      12      T
USUIRJFWND      16      M
ZAQMJRKLVS      16      M
PEQQROIUUS      16      M




"""