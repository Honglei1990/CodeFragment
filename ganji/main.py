from channel_extrack import url_list
from page_parsing import get_links_from
from multiprocessing import Pool
import time
from page_parsing import get_item_info
from page_parsing import URL_list
from page_parsing import item_info

item_all = [i['url'] for i in URL_list.find()]
item_any = [i['url'] for i in item_info.find()]
x = set(item_all)
y = set(item_any)
item_result = x - y


def get_links_from_urllist(channel):

    for num in range(1,101):
        try:
            while True:
                if get_links_from(channel,num)==None:
                    break
                else:
                    get_links_from(channel,num)
        except KeyboardInterrupt:
            break



if __name__ == "__main__":
    # get_item_infos(item_result)
    for i in item_result:
        try:
            get_item_info(i)
        except:
            print(i)
    print('结束!')
    # pool = Pool(processes=4)
    # pool.map(get_links_from_urllist,url_list.split())

#     for link in url_list.split():
#         get_links_from_urllist(link)