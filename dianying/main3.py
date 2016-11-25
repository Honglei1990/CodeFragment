from multiprocessing import Pool
from page_parsing3 import get_links_from
from page_parsing3 import get_links_from1
from channel_extrack3 import url_list
from page_parsing3 import get_item_info
import page_parsing3
from page_parsing3 import item_info
from page_parsing3 import URL_list

def get_links_from_urllist(channle):
    for num in range(2,101):
        get_links_from(channle,num)

def get_info_from_iteminfo(url):
    link_all = set(url)
    for link in link_all:
        try:
            get_item_info(link)
        except:
            print(link)

db_urls = [i['url'] for i in URL_list.find()]
index_urls = [i['url'] for i in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x - y

if __name__ == "__main__":
    # for i in url_list.split():
    #     get_links_from1(i)
    # pool = Pool(processes=8)
    # pool.map(get_links_from_urllist,url_list.split())
    # link_all = [i['url'] for i in page_parsing3.URL_list.find()]
    link_all = [i for i in rest_of_urls]
    print(rest_of_urls)

    get_info_from_iteminfo(link_all)


