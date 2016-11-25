import requests
from bs4 import BeautifulSoup

url = 'http://www.youxiangfuli.com/'

wb_data = requests.get(url)
soup = BeautifulSoup(wb_data.text, 'lxml')
logistics = soup.select('div.mytable_wrap > table > tbody > tr > td')
# print(logistics.text[0])
for i in logistics:
    print(i.text[0])

'''
div.mytable_wrap > table > tbody > tr > td
'''