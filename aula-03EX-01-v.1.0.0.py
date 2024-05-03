aluno=str(input("Digite o nome do aluno: "))
materia=str(input("Digite o nome da materia: "))
b1=float(input("Digite o a primeira nota: "))
b2=float(input("Digite o a primeira nota: "))
b3=float(input("Digite o a primeira nota: "))
b4=float(input("Digite o a primeira nota: "))

media = (b1+b2+b3+b4) / 4

if (media < 0) or (media > 10):
    mediaf = "Média inválida"
elif (media >= 7) and (media <= 10):
    mediaf = "Aprovado"
elif (media >= 5) and (media < 7):
    mediaf = "Recuperação"
else:
    mediaf = "Reprovado"

print(f"a media do aluno(a) {aluno} na materia {materia} foi {mediaf}")
