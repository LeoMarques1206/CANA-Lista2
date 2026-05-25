import random
import string

class Aluno:
    def __init__(self):
        self.nome = ''
        for i in range (0, 12, 1):
            self.nome = self.nome + random.choice(string.ascii_uppercase)
        self.matricula = ''
        for i in range (0, 6, 1):
            self.matricula = self.matricula + str(random.randint(0,9))
        self.creditos = random.randint(0,180)

def imprime(lista):
    for a in lista:
        print(a.nome, a.matricula, a.creditos, sep ='\t')
    print()

def ordenaCreditos(A):
    B = [None for i in range(0, len(A), 1)]
    C = [0 for i in range(181)]
    
    for a in A:
        C[a.creditos] += 1
        
    for i in range(1, 181):
        C[i] += C[i-1]
        
    for j in range(len(A)-1, -1, -1):
        C[A[j].creditos] -= 1
        B[C[A[j].creditos]] = A[j]
        
    return B

def ordenaMatricula(A):
    for p in range(5, -1, -1):
        B = [None for i in range(len(A))]
        C = [0 for i in range(10)]
        
        for a in A:
            d = int(a.matricula[p])
            C[d] += 1
            
        for i in range(1, 10):
            C[i] += C[i-1]
            
        for j in range(len(A)-1, -1, -1):
            d = int(A[j].matricula[p])
            C[d] -= 1
            B[C[d]] = A[j]
            
        A = B
        
    return A

def ordenaNome(A):
    for p in range(11, -1, -1):
        B = [None for i in range(len(A))]
        C = [0 for i in range(26)]
        
        for a in A:
            idx = ord(a.nome[p]) - 65
            C[idx] += 1
            
        for i in range(1, 26):
            C[i] += C[i-1]
            
        for j in range(len(A)-1, -1, -1):
            idx = ord(A[j].nome[p]) - 65
            C[idx] -= 1
            B[C[idx]] = A[j]
            
        A = B
        
    return A

n = 20
alunos = []
for i in range(0, 20, 1):
    alunos.append(Aluno())

print("ANTES DA ORDENACAO POR CREDITOS:")
imprime(alunos)
alunos = ordenaCreditos(alunos)
print("APOS A ORDENACAO POR CREDITOS:")
imprime(alunos)

print("ANTES DA ORDENACAO POR MATRICULA:")
imprime(alunos)
alunos = ordenaMatricula(alunos)
print("APOS A ORDENACAO POR MATRICULA:")
imprime(alunos)

print("ANTES DA ORDENACAO POR NOME:")
imprime(alunos)
alunos = ordenaNome(alunos)
print("APOS A ORDENACAO POR NOME:")
imprime(alunos)

"""
Passo 2

Saída: 

ANTES DA ORDENACAO POR CREDITOS:
LZIVXIJEPEJY    932076  180
REZKQWESTTKD    234407  125
HPLSYIRMTMGG    292425  39
CNYTYIHFGMDG    165659  144
BCQGMFECVWSS    839095  114
ZWEFVOKXSWEI    656003  33
BAFURZOVXIYP    573818  37
DDQKFAEOCOTV    420101  132
ZZESZMAXBKRB    351839  6
ZXTHJGDAWMWI    967827  154
KXGDQBOYBKRL    046056  143
PTUPXDYZTFME    046588  19
JRUZJQWEYKUO    856418  109
UONNXQVWBVEW    378064  112
PJDSTTRBGOYG    214600  11
OVWTYXVHXEJS    824001  67
CPQLKJVPUAEX    867938  53
VDYNNRHERWIK    257892  42
XDFLGKYBEVVF    987153  138
QOUEBBJCIRBJ    403060  178

ZZESZMAXBKRB    351839  6
PJDSTTRBGOYG    214600  11
PTUPXDYZTFME    046588  19
ZWEFVOKXSWEI    656003  33
BAFURZOVXIYP    573818  37
HPLSYIRMTMGG    292425  39
VDYNNRHERWIK    257892  42
CPQLKJVPUAEX    867938  53
OVWTYXVHXEJS    824001  67
JRUZJQWEYKUO    856418  109
UONNXQVWBVEW    378064  112
BCQGMFECVWSS    839095  114
REZKQWESTTKD    234407  125
DDQKFAEOCOTV    420101  132
XDFLGKYBEVVF    987153  138
KXGDQBOYBKRL    046056  143
CNYTYIHFGMDG    165659  144
ZXTHJGDAWMWI    967827  154
QOUEBBJCIRBJ    403060  178
LZIVXIJEPEJY    932076  180

Passo 3

Saída:

ANTES DA ORDENACAO POR MATRICULA:
ZZESZMAXBKRB    351839  6
PJDSTTRBGOYG    214600  11
PTUPXDYZTFME    046588  19
ZWEFVOKXSWEI    656003  33
BAFURZOVXIYP    573818  37
HPLSYIRMTMGG    292425  39
VDYNNRHERWIK    257892  42
CPQLKJVPUAEX    867938  53
OVWTYXVHXEJS    824001  67
JRUZJQWEYKUO    856418  109
UONNXQVWBVEW    378064  112
BCQGMFECVWSS    839095  114
REZKQWESTTKD    234407  125
DDQKFAEOCOTV    420101  132
XDFLGKYBEVVF    987153  138
KXGDQBOYBKRL    046056  143
CNYTYIHFGMDG    165659  144
ZXTHJGDAWMWI    967827  154
QOUEBBJCIRBJ    403060  178
LZIVXIJEPEJY    932076  180

APOS A ORDENACAO POR MATRICULA:
KXGDQBOYBKRL    046056  143
PTUPXDYZTFME    046588  19
CNYTYIHFGMDG    165659  144
PJDSTTRBGOYG    214600  11
REZKQWESTTKD    234407  125
VDYNNRHERWIK    257892  42
HPLSYIRMTMGG    292425  39
ZZESZMAXBKRB    351839  6
UONNXQVWBVEW    378064  112
QOUEBBJCIRBJ    403060  178
DDQKFAEOCOTV    420101  132
BAFURZOVXIYP    573818  37
ZWEFVOKXSWEI    656003  33
OVWTYXVHXEJS    824001  67
BCQGMFECVWSS    839095  114
JRUZJQWEYKUO    856418  109
CPQLKJVPUAEX    867938  53
LZIVXIJEPEJY    932076  180
ZXTHJGDAWMWI    967827  154
XDFLGKYBEVVF    987153  138

Passo 4

Saída:

ANTES DA ORDENACAO POR NOME:
KXGDQBOYBKRL    046056  143
PTUPXDYZTFME    046588  19
CNYTYIHFGMDG    165659  144
PJDSTTRBGOYG    214600  11
REZKQWESTTKD    234407  125
VDYNNRHERWIK    257892  42
HPLSYIRMTMGG    292425  39
ZZESZMAXBKRB    351839  6
UONNXQVWBVEW    378064  112
QOUEBBJCIRBJ    403060  178
DDQKFAEOCOTV    420101  132
BAFURZOVXIYP    573818  37
ZWEFVOKXSWEI    656003  33
OVWTYXVHXEJS    824001  67
BCQGMFECVWSS    839095  114
JRUZJQWEYKUO    856418  109
CPQLKJVPUAEX    867938  53
LZIVXIJEPEJY    932076  180
ZXTHJGDAWMWI    967827  154
XDFLGKYBEVVF    987153  138

APOS A ORDENACAO POR NOME:
BAFURZOVXIYP    573818  37
BCQGMFECVWSS    839095  114
CNYTYIHFGMDG    165659  144
CPQLKJVPUAEX    867938  53
DDQKFAEOCOTV    420101  132
HPLSYIRMTMGG    292425  39
JRUZJQWEYKUO    856418  109
KXGDQBOYBKRL    046056  143
LZIVXIJEPEJY    932076  180
OVWTYXVHXEJS    824001  67
PJDSTTRBGOYG    214600  11
PTUPXDYZTFME    046588  19
QOUEBBJCIRBJ    403060  178
REZKQWESTTKD    234407  125
UONNXQVWBVEW    378064  112
VDYNNRHERWIK    257892  42
XDFLGKYBEVVF    987153  138
ZWEFVOKXSWEI    656003  33
ZXTHJGDAWMWI    967827  154
ZZESZMAXBKRB    351839  6


"""