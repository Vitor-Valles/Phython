"""
Programa: Cálculo do INSS
Autor: Paulo Henrique
Licença: GNU
Data: 2024/05/07
Versão: v1
Descrição: Este programa terá como proposta calcular o INSS de um salário.
"""

nome = str(input("Qual o nome?\n"))
cargo = str(input("Qual o cargo?\n"))
salB = float(input("Digite o salário bruto?\n"))

dependentes=[]

dpC = int(input("Dependente conjugue renda anual ate 27mil:\n1 - sim\n2 - não\n"))
 
while (dpC < 1 or dpC > 2):
    print("ERRO - valor de entrada invalido!")
    dpC = int(input("Dependente conjugue renda anual ate 27mil:\n1 - sim\n2 - não"))
 
if (dpC == 1):
    nomeC = str(input("Digite o nome do conjugue:\n"))

    dependentes.append(nomeC)

 
dpF21 = int(input("Dependente filho(a) <= 21 ou Deficiente:\n1 - sim\n2 - não"))
 
while (dpF21 < 1 or dpC > 2):
    print("ERRO - valor de entrada invalido!")
    dpF21 = int(input("Dependente filho(a) <= 21 ou Deficiente:\n1 - sim\n2 - não"))
 
while (dpF21 == 1):
    nomeD = str(input("Digite o nome do filho(a):\n"))
    dependentes.append(nomeD)
    dpF21 = int(input("Dependente filho(a) <= 21 ou Deficiente:\n1 - sim\n2 - não"))
 
    while (dpF21 < 1 or dpC > 2):
        print("ERRO - valor de entrada invalido!")
        dpF21 = int(input("Dependente filho(a) <= 21 ou Deficiente:\n1 - sim\n2 - não"))
 
dpF18 = int(input("Dependente filho(a) < 18:\n1 - sim\n2 - não"))
 
while (dpF21 < 1 or dpC > 2):
    print("ERRO - valor de entrada invalido!")
    dpF18 = int(input("Dependente filho(a) < 18:\n1 - sim\n2 - não"))
 
while (dpF21 == 1):
    dependentes.append(nomeD)
    nomeD = str(input("Digite o nome do filho(a):\n"))
 
    dpF18 = int(input("Dependente filho(a) < 18:\n1 - sim\n2 - não"))
 
    while (dpF21 < 1 or dpC > 2):
        print("ERRO - valor de entrada invalido!")
        dpF18 = int(input("Dependente filho(a) < 18:\n1 - sim\n2 - não"))
 


while (salB <= 0):
    print("ERRO - Valor inválido!!")
    salB = float(input("Digite o salário bruto?\n"))

if (salB <= 1412):
    inss = salB * 0.075
elif (salB <= 2666.68):
    inss = salB * 0.09
elif (salB <= 4000.03):
    inss = salB * 0.12
elif (salB <= 7786.02):
    inss = salB * 0.14
else:
    inss = 1200



print(f"Nome: {nome}\nCargo: {cargo}\nSalário bruto: {salB}\nValor do INSS: {inss} \nO nome do conjuge é os depedentes e {dependentes} ")