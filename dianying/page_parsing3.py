from bs4 import BeautifulSoup
import requests
import pymongo
import random
from channel_extrack3 import url_list
import time

client = pymongo.MongoClient('localhost',27017)
Movies = client['Movies']
URL_list = Movies['URL_list']
item_info = Movies['item_info']

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Connection': 'keep-alive'
}
proxy_list = [
    '58.222.254.11:3128',
    '218.26.219.186:8080',
    '218.75.100.114:8080'
]
proxy_ip = random.choice(proxy_list)
proxies = {'http':proxy_ip}

def get_links_from(channel,page):
    list_view = "{}index_{}.html".format(channel,str(page))
    wb_data = requests.get(list_view)
    wb_data.encoding = wb_data.apparent_encoding
    time.sleep(3)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('td > b > a')
    for link in links:
        if link.get('title'):
            URL_list.insert_one({'url':'http://www.dy2018.com'+link.get('href')})
            print({'url':'http://www.dy2018.com'+ link.get('href')})
        else:
            pass
            # Nothing !
    #     print('http://www.dy2018.com'+link)
    # print(links)
def get_links_from1(channel):
    wb_data = requests.get(channel)
    wb_data.encoding = wb_data.apparent_encoding
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('td > b > a')
    for link in links:
        URL_list.insert_one({'url':'http://www.dy2018.com/'+link.get('href')})

def get_item_info(url):
    wb_data = requests.get(url,headers=headers)
    wb_data.encoding = wb_data.apparent_encoding
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if wb_data.status_code == 404:
        pass
    else:
        title = soup.select('div.title_all > h1')[0].text
        rank = soup.select('div.position > span > strong.rank')[0].text if soup.find_all('strong', 'rank') else None
        if soup.find_all('span', 'updatetime'):
            date = soup.select('span.updatetime')
            postdate = ''.join((date[0].text.split('：')[1]).split('-'))
        else:
            postdate = None
        thunderdown = soup.select('tbody > tr a')[0].text if soup.find_all('strong','rank') else None
        position = list(soup.select('div.position > span > a')[0].stripped_strings) if soup.find_all('span','a') else None
        # try:
        item_info.insert_one({"title":title,\
                              "rank":rank,\
                              "postdate":postdate,\
                              "thunderdown":thunderdown,"position":position,'url':url})
    # try:
    # print({"title":title,"rank":rank,"postdate":postdate,\
    #                       "thunderdown":thunderdown,"position":position,'url':url})
    # except IndexError as e:
    #     pass

# get_item_info('http://www.dy2018.com/html/gndy/jddy/53164.html')
# get_item_info('http://www.dy2018.com/i/97428.html')
# get_links_from('http://www.dy2018.com/html/tv/rihantv/',2)
