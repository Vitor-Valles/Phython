aluno=str(input("Digite o nome do aluno(a):\n"))
materia=(input("Digite a matéria:\n"))
#Estrutura de repetição para ver se o numero e valido
n1=float(input("Digite a nota da 1º avaliação:\n"))
while (n1 > 10) or (n1 < 0):
    print(f"nota invalidao")
    n1=float(input("Digite a nota da 1º avaliação:\n"))
n2=float(input("Digite a nota da 2º avaliação:\n"))  
while (n2 > 10) or (n2 < 0):
    print(f"nota invalida")
    n2=float(input("Digite a nota da 2º avaliação:\n"))
n3=float(input("Digite a nota da 3º avaliação:\n"))
while (n3 > 10) or (n3 < 0):
    print(f"nota invalida")
    n3=float(input("Digite a nota da 3º avaliação:\n")) 
n4=float(input("Digite a nota da 4º avaliação:\n"))
while (n4 > 10) or (n4 < 0):
    print(f"nota invalida")
    n4=float(input("Digite a nota da 4º avaliação:\n"))

#Processar o valor da média baseado nas notas
media=(n1+n2+n3+n4)/4

#estrutura condicional simples
if (media < 0) or (media > 10):
    mediaf = "Média inválida"
elif (media >= 7) and (media <= 10):
    mediaf = "Aprovado"
elif (media >= 5) and (media < 7):
    mediaf = "Recuperação"
else:
    mediaf = "Reprovado"

print(f"a media do aluno(a) {aluno} na materia {materia} foi de {media} obtendo o resultado: {mediaf}")
