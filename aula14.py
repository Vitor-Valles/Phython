#Instalar a biblioteca do panda
    #python -m pip install matplotlib
import matplotlib.pyplot as plt

#Construindo um gráfico na mão

#Vetores para minhas medições de x e y
x = [1,2,3,4,5,6]
y = [0,20,30,40,50,60]

plt.plot(x,y,label='Dados',color='y',linestyle='solid', lw=2.0)

plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.title('Titulo do gráfico')

plt.xticks([0,1,2,3,4,5,6,7])
plt.yticks([0,20,40,60])

plt.legend('Legenda')

plt.show()