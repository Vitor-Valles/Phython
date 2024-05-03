#Importando uma biblioteca randomica
import random

#randint -> randomico do tipo inteiro
numero=random.randint(1,100)

escolha=0
tentativas=0

while (escolha != numero):
    escolha=int(input("Entre com um numero de 0 até 100:\n"))

    tentativas += 1

    if(escolha < numero):
        print(f"O número {escolha}, é menor que o sorteado!!!")
    elif(escolha > numero):
        print(f"O número{escolha}, é maior que o sorteado!!!")
    else:
        print(f"O número {escolha} foi o sorteado!!!")
else:
    print(f"Voce acertou com {tentativas}, tentaivas!!!")