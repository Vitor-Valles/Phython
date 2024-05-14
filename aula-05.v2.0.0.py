"""
Construindo funções para uma calculadora
"""
def soma(a,b):
    resp = a + b
    return resp
def subtracao (a,b):
    return a - b
def multiplicacao (a,b):
    return a * b
def divisao(a,b):
    if b != 0:
        return a / b
    else:
        return "ERRO: Divisão por zero"
    
# função para calculadora
def calculadora():
    print("bem-vindo á calculadora")
    while True:
        print("Escolha a operação\n1 - adição\n2 - subtração\n3 - multiplicação\n4 - divisão\n5 - sair")
        opecao = int(input("Digite a opção desejada: "))

        if(opecao==5):
            print("Obriagado por utilizar nossa calculadora!!!")
            break
        num1=float(input("Digite o primeiro número "))
        num2=float(input("Digite o segundo número "))

        if(opecao==1):
            result = soma(num1,num2)
            print(f"Resultado é {result}")
        elif(opecao==2):
            result = subtracao(num1,num2)
            print(f"Resultado é {result}")
        elif(opecao==3):
            result = multiplicacao(num1,num2)
            print(f"Resultado é {result}")
        elif(opecao==4):
            result = divisao(num1,num2)
            print(f"Resultado é {result}")
        else:
            print("ERRO - opção invalida!!")

#chama a função principal
calculadora()