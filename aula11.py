# Instalar a biblioteca do panda
# python -m pip install pandas
# python -m pip install openpyxl
import pandas as pd 

#Criando vetor como objeto
vetor = {
    'Nome':[
        'Vitor',
        'Paulo',
        'Renato'        
    ],
    'Idade':[
        18,
        19,
        1000
    ]
}

# Criar uma variavel para receber os dados do vetor e encapsular dentro de um DataFrame
dados = pd.DataFrame(data=vetor)

#Criar o arquvo do Execel
dados.to_excel('NomesAula-11.xlsx',index=False)

print(dados)
