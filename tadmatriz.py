def cria(lin, col):

    matriz = {}

    for i in range(1, lin+1):
        matriz[i] = []
        for j in range(col):
            matriz[i].append(0)
    return matriz

def getElem(matriz, lin, col):
    if lin in matriz.keys() and len(matriz[lin]) >= col:
        return matriz[lin][col-1]

    return None

def setElem(matriz, lin, col, valor):
    if lin in matriz.keys() and len(matriz[lin]) >= col:
        matriz[lin][col-1] = valor
        return matriz

    return None

def soma(matrizA,matrizB):
    if len(matrizA.keys()) == len(matrizB.keys()) and len(matrizA[1]) == len(matrizB[1]):
        matrizC = {}
        for i in range(1,len(matrizA)+1):
            matrizC[i] = []
            for j in range(len(matrizA[i])):
                matrizC[i].append(float(matrizA[i][j]) + float(matrizB[i][j]))
        return matrizC

    return None

def vezesK(matrizA,K):
        for i in range(1,len(matrizA.keys())+1):
            for j in range(len(matrizA[i])):
                matrizA[i][j] = matrizA[i][j] * K
        return matrizA

def clona(matriz):
    matrizC = {}
    matrizC = matriz
    return matrizC

def diagP(matriz):
    
    if len(matriz.keys()) == len(matriz[1]):
        lst_saida = []
        for i in range(1,len(matriz)+1):
            lst_saida.append(matriz[i][i-1])
        return lst_saida

    return None

def diagS(matriz):

    if len(matriz.keys()) == len(matriz[1]):
        lst_saida = []
        for i in range(1,len(matriz)+1):
            lst_saida.append(matriz[i][len(matriz[i])-i])
        return lst_saida

    return None

def quantLinhas(matriz):
    return len(matriz)

def quantColunas(matriz):
    return len(matriz[1])

def carregamat(arquivo):
    arquivo = open(arquivo,'r')
    matriz = {}
    indicelinha = 1
    for linha in arquivo.readlines():

        linhalimpa = linha.strip()
        numeros = linhalimpa.split()
        matriz[indicelinha] = []
        for i in numeros:
            matriz[indicelinha].append(i)
        indicelinha += 1
    arquivo.close()
    return matriz

def salvamat(matriz,arquivo):
    arquivo = open(arquivo,'w')
    for i in matriz.keys():
        for j in matriz[i]:
            arquivo.write(str(j))
            arquivo.write(' ')
        arquivo.write('\n')
    arquivo.close()

def tostring(matriz):
    strsaida = ''
    contlinhas = 0
    for i in matriz.keys():
        for j in matriz[i]:
            strsaida += str(j)
            strsaida += ' '
        contlinhas += 1
        if contlinhas < len(matriz.keys()):
            strsaida += '\n'
    return strsaida

def multi(matriz1,matriz2):
    if len(matriz1[1]) == len(matriz2):
        matrizsaida = {}
        soma = 0.0
        for numlinha in range(1,len(matriz1)+1):
            matrizsaida[numlinha] = []
            for i in range(len(matriz2[1])):
                for numcoluna in range(len(matriz2)):
                    soma += float(matriz1[numlinha][numcoluna]) * float(matriz2[numcoluna+1][i])
                matrizsaida[numlinha].append(soma)
                soma = 0
        return matrizsaida

    return None

def transposta(matriz):
    matrizsaida = {}
    for coluna in range(len(matriz[1])):
        matrizsaida[coluna+1] = []
        for linha in range(1,len(matriz)+1):
            matrizsaida[coluna+1].append(matriz[linha][coluna])
    return matrizsaida
