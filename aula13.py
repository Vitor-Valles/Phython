#Instalar a biblioteca do panda
    #python -m pip install matplotlib
import matplotlib.pyplot as plt

"""
Dados ficticios de exemplo do indice da bovespa (podendo ser subistituido por valores reais) 
Lista de valores em um vetor
"""
dadosBovespa=[
    100,102,105,103,101,122,115,111,112
]

intervaloTempo = range(0,len(dadosBovespa))

#Plotar o gráfico da linhas
plt.plot(intervaloTempo, dadosBovespa)

plt.xlabel('Tempo (60min)')
plt.ylabel('valor do indice')
plt.title('Ìndice BOVESPA - Time Frame - 60min')
plt.show()