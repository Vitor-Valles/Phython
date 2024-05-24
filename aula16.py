#Instalar a biblioteca do pandas yfanance matplolib
    #python -m pip install pandas
    #python -m pip install yfinance
    #python -m pip install matplotlib
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Função para obter os dados da B3
def obter_dados(ticker, periodo='10y'):
    # Obter dados historicos do ticker
    dados = yf.download(ticker, period = periodo)
    return dados

# Armazenar dadpos em uma Matriz (DataFrame do pandas)
def armazena_dados(dados):
    return dados

# Gerar gráfico de dadosz
def gerar_grafico(dados, ticker):
    plt.figure(figsize=(10,5))
    plt.plot(dados.index, dados['Close'],label="Fechamento")
    plt.title(f'Preço de Fechamento do {ticker}')
    plt.xlabel('data')
    plt.ylabel('Preço (R$)')
    plt.legend()
    plt.grid()
    # Salvar o gráfico com imagem .PNG
    plt.savefig(f'{ticker}_grafico.png')
    plt.show()

# Gravar os dados em uma  planilha de Excel
def grava_em_excel(dados, nome_arquivo):
    # Grava o DataFrame em uma planilhar Excel
    dados.to_excel(nome_arquivo, engine='openpyxl', index=True)
    print(f'Dados gravados em {nome_arquivo}')

# Uso

if __name__ == "__main__":
    # Exemplo PETROBRAS
    ticker = "PETR4.SA"
    dados = obter_dados(ticker)
    matriz_dados = armazena_dados(dados)

    # Nome arquivo Excel
    nome_arquivo = "dados_bolsa.xlsx"

    # Grava na planilha do Excel
    grava_em_excel(matriz_dados, nome_arquivo)

    # Gerar gráfico
    gerar_grafico(matriz_dados, ticker)
