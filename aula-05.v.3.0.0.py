j = 0
linha = [
    "fruta"
    "Qtd"
    "Preço"
]
matriz = []

matriz.append(linha)

while True:
    print("Escolha a operação\n1 - adicionar\n2 - sair ")
    opcao = int(input("Digite a opção: "))

    if opcao == 2:
        break

    linha.append(input("Digite o nome da fruta: "))
    linha.append(input("Digite a quantidade: "))
    linha.append(input("Digite o preço: "))

    matriz.append(linha)

nL = len(matriz)

for i in range(nL):
    print(f"{matriz[i][0]}|{matriz[i][1]}|{matriz[i][2]}")