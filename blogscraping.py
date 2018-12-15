import requests
from bs4 import BeautifulSoup
from csv import writer

resqponse = requests.get('https://medium.com/')

soup = BeautifulSoup(resqponse.text,'html.parser')
articles = soup.select('.ui-h3')
for article in articles:
    print(article.get_text())
