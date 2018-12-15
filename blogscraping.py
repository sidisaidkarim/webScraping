import requests
from bs4 import BeautifulSoup
from csv import writer

url = 'https://wordpress.org/plugins/ecommerce/marketing/page/{}/'
plug_list = []
for i in range(2,110):
    page = i
    url_page = url.format(page)
    response = requests.get(url_page)
    soup = BeautifulSoup(response.text,'html.parser')
    plugins = soup.select('.entry')
    for plugin in plugins:
        name = plugin.find('a').get_text().replace('\n',' ')
        plug_list.append(name)


with open('wp_ecommerce_plugins.csv','w',encoding="utf-8") as csv_file:
    csv_writer = writer(csv_file)
    headers = ['plugin name']
    csv_writer.writerow(headers)
    for pg in plug_list:
        csv_writer.writerow([pg])
        
  
    
    
