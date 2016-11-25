import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'Connection': 'keep-alive'
}
url = 'https://kyfw.12306.cn/otn/leftTicket/init'

wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text, 'lxml')
zuowei = soup.select('tbody > tr > td')
print(zuowei.text)