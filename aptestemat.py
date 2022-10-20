from tadmatriz import carregamat,multi, salvamat,soma, tostring,transposta

def main():
    tadmatrizA = carregamat('A.txt')
    tadmatrizB = carregamat('B.txt')
    tadmatrizC = carregamat('C.txt')
    tadmatrizD = carregamat('D.txt')
    AxB = multi(tadmatrizA,tadmatrizB)
    salvamat(AxB,'AxB.txt')
    CmaisD = soma(tadmatrizC,tadmatrizD)
    salvamat(CmaisD,'CmaisD.txt')
    BxD = multi(tadmatrizB,tadmatrizD)
    salvamat(BxD,'BxD.txt')
    tadmatrizAxB = carregamat('AxB.txt')
    tadmatrizCmaisD = carregamat('CmaisD.txt')
    tadmatrizBxD = carregamat('BxD.txt')
    transpostamatrizAxB = transposta(tadmatrizAxB)
    transpostamatrizBxD = transposta(tadmatrizBxD)
    transpostamatrizCmaisD = transposta(tadmatrizCmaisD)
    print(tostring(transpostamatrizAxB))
    print(tostring(transpostamatrizBxD))
    print(tostring(transpostamatrizCmaisD))

main()