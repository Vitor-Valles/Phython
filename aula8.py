# importar para o projeto
# python -m pip install BeautifulSoup4
# python -m pip install requests
#Importar para o projeto
import requests
from bs4 import BeautifulSoup

url = 'https://www.vgmusic.com/music/console/nintendo/nes/'

#Varivale para o parametro da url
htmlText = requests.get(url).text

soup = BeautifulSoup(htmlText,'html.parser')

for link in soup.find_all('a'):
    print(link.get('href'))