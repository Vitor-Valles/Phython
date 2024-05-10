# criando um vetor e já com valore atribuidos
frutas=[
    "Banana",
    "Melão",
    "Caqui",
    "Uva",
    "Maçã",
    "Tomate"
]
print(f"Posição 3 é: {frutas[3]}")
compra = frutas[2]
print(f"O valor era {compra}")
venda="perâ"
frutas[5]=venda
print(f"o valor mudou para {frutas[5]}")

# frutas[7]="Melância" --Não é assim
# Adiciona no vetor
frutas.append("Melância")
print(f"A fruta adicionado é {frutas[6]}")

# removendo uma posição no vetor
frutas.remove("Melão")
print(f"Nova posição é {frutas[1]}")

# Quantidade de linhas de index do vetor
linhas= len(frutas)
print(f"quantidade de indices é {linhas}")
