import requests
from bs4 import BeautifulSoup
import pymongo
import channel_extrack


Client = pymongo.MongoClient('localhost', 27017)
myDB = Client['myDB']
URL_list = myDB['URL_list']
item_info = myDB['item_info']

def get_links_from(channel,page):
    list_view = "{}o{}".format(channel,str(page))
    wb_data = requests.get(list_view)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # links = soup.select('div.js-item > a')
    # links1 = soup.select('td.t a')
    # print(links1)
    if soup.select('div.noinfo'):
        pass
    else:
        links = soup.select('div.js-item > a')
        links1 = soup.select('td.t a')
        links.extend(links1)
        for link in links:
            URL_list.insert_one({'url':link.get('href').split('?')[0]})



def get_item_info(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    item_info.insert_one({"title":soup.title.text.strip(), "price":soup.select('span.price_now i')[0].text, \
                          'area': soup.select('div.palce_li span i')[0].text, 'url': url})


    # print({"title":soup.title.text.strip(), "price":soup.select('span.price_now i')[0].text, \
    #                       'area': soup.select('div.palce_li span i')[0].text, 'url': url})



# get_links_from('http://bj.ganji.com/jiaju/',1)
# get_item_info('http://zhuanzhuan.ganji.com/detail/778858770874155011z.shtml')
