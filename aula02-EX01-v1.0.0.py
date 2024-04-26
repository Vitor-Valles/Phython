"""
Comentario em bloco

Programa: Média de aluno
Autor: Vitor Andrade Valles
Licença: GNU
Data: 2024/04/26
Versão: v1
Descrição: Este programa tera como proposta calcular a média do aluno e sua materia
"""


nome=(input("digite o nome do funcionario: "))
cargo=(input("digite o cargo do funcionario: "))
depart=(input("digite o departamento do funcionario: "))
salb=float(input("digite o salario bruto do funcionario: "))

if salb < 1600:
    novosal=float(salb*1.085)
else:   
    novosal=float(salb*1.07)
print(f"o funcionario {nome} do cargo {cargo} no departamento {depart} teve um novo salario de:{novosal} ")

