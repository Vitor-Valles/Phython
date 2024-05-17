# importar para o projeto
# python -m pip install BeautifulSoup4
# python -m pip install requests
import requests
from bs4 import BeautifulSoup

# Coletar para analisar a primeira pagina de cotações
page = requests.get('https://valorinveste.globo.com/cotacoes/')
soup = BeautifulSoup(page.text,'html.parser')

#Passar a classe para a varivel
acao = soup.find(class_='vd-table')

#Pegar todas as instancias da tag TD dentro da classe=vd-table
acaoItens= acao.find_all('td')

print(acaoItens)

response = page.text
responseStatus = page

# Verificamos se foi bem-sucedida a comunicação 

if responseStatus.status_code == 200:
    #Criar um objeto BeautifulSoup com todo o conteúdo da pagina HTLM
    soup = BeautifulSoup(responseStatus.content, 'html.parser')
    #Econtre elementos específicos na página usando os seletores do CSS
    #Vamos pegar todos os link´s desta pagina
    links = soup.select('a')

    # Imprimir todos os seus atributos
    for link in links:
        href = link.get('href')
        text = link.get_text()
        print(f"{text}")
        print(f"URL do link {href}\n\n\n")
else:
    print("Falha na requisição  HTTPS")