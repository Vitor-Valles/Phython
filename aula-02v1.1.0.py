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
"""
Igual ---> ==
Menor que ---> <
Maior que ---> >
Menor igual ---> <=
Maior igual ----> >=
Deferente (o simbolo e um = com um / no meio)
Igualdade absoluta ---> === 
Diferença absoluta ---> !==

"""
#Criar as variaveis para entrada de dados do aluno
#o input serve para receber dados que o usuario insiriu
nome=str(input("Digite o nome do aluno(a):\n"))
materia=(input("Digite a matéria:\n"))
n1=float(input("Digite a nota da 1º avaliação:\n"))
n2=float(input("Digite a nota da 2º avaliação:\n"))
n3=float(input("Digite a nota da 3º avaliação:\n"))

#Processar o valor da média baseado nas notas
nf=(n1+n2+n3)/3
#Escreva a saida o nome materia e a média
#O f e uma função para escrita
print(f'O(A) aluno {nome} na materia {materia} obteve a média:{nf}')
