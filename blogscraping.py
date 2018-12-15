import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://wordpress.org/plugins/search/ecommerce/page/{}/'
for i in range(2,20):
    page = i
    url_page = url.format(page)
    response = requests.get(url_page)
    soup = BeautifulSoup(response.text,'html.parser')
   
    with open('ecommerce_plugins_wp.csv','w') as csv_file:
        csv_writer = writer(csv_file)
        headers = ['plugin name']
        csv_writer.writerow(headers)
        plugins = soup.select('.entry')
        for plugin in plugins:
            name = plugin.find('a').get_text().replace('-',' ')
            csv_writer.writerow([name])
    
    
