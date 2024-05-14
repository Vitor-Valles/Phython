# Criando matriz bi-dimensional
feira = [
    ["Maçã", 5, 10, 50],
    ["Banana", 12, 0.6, 8],
    ["Perâ", 6, 1, 6],
    ["Melância", 3, 2, 6]
]

print(f"O valor da linha 1 e coluna 1 é: {feira[1][1]}")

feira[2][0] = "Uva"
print(f"O valor da fruta perâ mudou para: {feira[2][0]}")

compra = feira[3][3]
print(f"Valor da compra de {feira[3][0]} é de R$ {compra}")

# Construindo Matriz com uso de funções
def main ():
    a = ler_matriz ()
    if simetrica (a):
        print("Matriz simétrica")
    else:
        print("Matriz não é simétrica")

def ler_matriz ():
    numL = int(input("Digite o número de linhas da matriz:\n"))
    numC = int(input("Digite o número de colunas da matriz:\n"))

    matriz = []
    for i in range (numL):
        linha = []
        for j in range (numC):
            # (%d, %d) %i (i, j) Expressão regular 
            valorC = input("Digite o valor do elemento em (%d, %d):\n"%(i, j))
            linha.append(valorC)
        matriz.append(linha)
    return matriz

def simetrica (matriz):
    numL = len (matriz)
    numC = len (matriz[0])

    if (numL != numC):
        return False
    for i in range (numL):
        for j in range (i):
            if (matriz[i][j] != matriz[i][j]):
                return False
    return True

main ()