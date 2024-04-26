"""
Comentario em bloco

Programa: Média de aluno
Autor: Vitor Andrade Valles
Licença: GNU
Data: 2024/04/26
Versão: v1
Descrição: Este programa tera como proposta calcular a média do aluno e sua materia
"""

"""
Operadores matematicos(aritimeticos) 

Multiplição --->  ( * )
Divisão ---> ( / )
Soma ---> ( + )
Subtração ---> ( - )
""" 
#Criar as variaveis para entrada de dados do aluno

nome="Vitor"
materia="Programação"
n1=float(5.8)
n2=float(8)
n3=float(6.5)

#Processar o valor da media baseado nas notas
nf=(n1+n2+n3)/3
#Escreva a saida o nome materia e a média
#O f e uma função para escrita
print(f'O(A) aluno {nome} na materia {materia} obteve a média:{nf}')