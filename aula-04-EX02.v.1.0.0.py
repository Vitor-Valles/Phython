"""
Criar um programa que apos a entrade do nome, cargo, salrio bruto, calule o INSS
ate 1412 - 7.5%
ate 2666.69 - 9%
ate 4000.03 - 12%
ate 7786,02 - 14%
acima fixo em 1200.00 //não sei se e real

caso o usuario tenha depedentes ele deve unformar o nome de cada dependente menor dce 18 anos ou até 21 anos caso esteja na faculdade ou deficiente. conjuge que tenha
renda inferior a 27mil por anos entra como dependente
"""

nome = str (input("Digite o nome do funcionario:\n"))
cargo = str (input("Digite o cargo do funcionario:\n"))
sallb = float (input("Digite o salario do funcionario\n"))

while(sallb < 0):
    print("Erro salario invalido digite novamente.")
    sallb = float (input("Digite o salario do funcionario\n"))

if (sallb <= 1422):
    inss = sallb * 0.075
elif(sallb <= 2666.68):
    inss = sallb * 0.09
elif(sallb <= 4000.03):
    inss = sallb * 0.12
elif(sallb <= 7786.02):
    inss = sallb * 0.14
else:
    inss = 1200
print(f"funcionario: {nome}\ncargo: {cargo} \nsalario bruto {sallb} \nvalor INSS {inss}")