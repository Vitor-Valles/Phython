#Instalar a biblioteca do panda
    #python -m pip install pandas
    #python -m pip install openpyxl
    #python -m pip install matplotlib
import pandas as pd
import matplotlib.pyplot as plt
# Criar uma variavel para recebar a planilha do excel
x = pd.read_excel('C:/Users/vitor.avalles/Desktop/Python/DadosAula-12.xlsx')

#Criando gráfico
#Adicionar o titulo do gráfico
plt.suptitle("Vendas Região - Mensal", fontsize=15, weight='bold')

plt.plot(x['Valor Final'])

#Imprimir o gráfico
plt.show()