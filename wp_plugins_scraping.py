import requests
from bs4 import BeautifulSoup
from csv import writer
import re

#wp plugins search url , replcae keyword after /search
url = 'https://wordpress.org/plugins/search/contact/page/{}/'
plug_list = []
#loop through pages 
for i in range(2,100):
    page = i
    url_page = url.format(page)
    response = requests.get(url_page)
    soup = BeautifulSoup(response.text,'html.parser')
    plugins = soup.find_all('article')
    for plugin in plugins:
        name = plugin.find('h2').get_text().replace('\n',' ')
        #get active installation text, than remove text and get int value
        text_istallation= plugin.find(class_="active-installs" ).get_text().replace('\n','')
        nb_istallation = re.sub('\n|\t|\+ active installations','',text_istallation)
        nb_istallation2 = re.sub('\+ million active installations','000000',nb_istallation)
        nb_istallation3 = re.sub('Fewer than 10 active installations','10',nb_istallation2)
        nb_int = re.sub(',','',nb_istallation3)
        plug_list.append( [name ,int(nb_int)] )
#wirte csv file
with open('wp_conntact_plugins.csv','w',encoding="utf-8") as csv_file:
    csv_writer = writer(csv_file)
    headers = ['plugin name','active installations']
    csv_writer.writerow(headers)
    for pg in plug_list:
        csv_writer.writerow( [pg[0],pg[1]])

        
  
    
    
