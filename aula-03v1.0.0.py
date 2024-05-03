#Conhecendo a estrutura condicional CASO

#Entrada de dados
dia = 7

#Match no Python significa a estrutura Caso
#Estrutura condiconal Caso
match dia:
    case 1:
        diaSemana="Domingo"
    case 2:
        diaSemana="Segunda-Feira"
    case 3:
        diaSemana="Terça-Feira"
    case 4:
        diaSemana="Quarta-Feira"
    case 5:
        diaSemana="Quinta-Feira"
    case 6:
        diaSemana="Sexta-Feira"
    case 7:
        diaSemana="Sábado"
    case _:
        diaSemana="Este dia da semana não existe"

print(f'Dia da semana é {diaSemana}')

#Estrutura else if no Python e elif
if (diaSemana=="Sábado"):
    atividade = "Dormir após a festa."
elif (diaSemana=="Domingo"):
    atividade = "Churrasco."
else:
    atividade="Trabalhar."

print(f"hojé e: {diaSemana}, logo dia de {atividade}")