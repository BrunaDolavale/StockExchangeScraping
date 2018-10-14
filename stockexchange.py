from urllib.request import urlopen
import csv
from datetime import datetime
from bs4 import BeautifulSoup

pagina_de_cotacao = 'http://www.bloomberg.com/quote/SPX:IND'
pagina = urlopen(pagina_de_cotacao)

soup = BeautifulSoup(pagina, 'html.parser')
nome_cotacao = soup.find('h1', attrs={'class': 'name'})

nome = nome_cotacao.text.strip()
print(nome)
preco_cotacao = soup.find('div', attrs={'class':'price'})
preco = preco_cotacao.text
print(preco)


 
paginas_de_cotacao = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND', 'https://www.bloomberg.com/quote/IBOV:IND']

dados = []
for cotacao in paginas_de_cotacao:
    pagina = urlopen(cotacao)
    soup = BeautifulSoup(pagina, 'html.parser')
    nome_cotacao = soup.find('h1', attrs={'class': 'name'})
    nome = nome_cotacao.text.strip()
    preco_cotacao = soup.find('div', attrs={'class':'price'})
    preco = preco_cotacao.text.strip()
    dados.append((nome, preco))

with open('teste.csv', 'a') as csv_file:
 writer = csv.writer(csv_file)
 for nome, preco in dados:
     writer.writerow([nome, preco, datetime.now()])