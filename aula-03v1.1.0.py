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

#Estrutura else if no Python e elif
if (diaSemana=="Sábado"):
    atividade = "Dormir após a festa."
elif (diaSemana=="Domingo"):
    atividade = "Churrasco."
else:
    atividade="Trabalhar."

if(diaSemana=="Este dia da samana não existe"):
    print(f'{diaSemana}')
elif(diaSemana=="Sábado"):
    atividade='Dormir apos a festa'
    print(f"Hojé:{diaSemana}, logo dia de {atividade}.")
elif (diaSemana=="Domingo"):
    atividade="Churrasco"
    print(f"Hojé:{diaSemana}, logo dia de {atividade}.")
else:
    atividade="tabalhar"
    print(f"Hojé:{diaSemana}, logo dia de {atividade}.")
"""
Estrutura de Tabela-verdade


E->Conjunção -->Dois lado tem que ser verdadeiro para o resultado seer verdadeiro
VEV=V
FEV=F
VEF=F
FEF=F

OU->Dinjunção -->Um lado tem que ser verdadeiro para o resultado seer verdadeiro
VEV=V
FEV=V
VEF=V
FEF=F

Não->Negação -->O resultado por exemplo for verdadeiro ele se torna falso o mesmo com o oposto
VEV=V=F
FEV=F=V
VEF=F=V
FEF=F=V
"""