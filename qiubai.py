# _*_ coding:utf-8 _*_
import requests
from bs4 import BeautifulSoup

page='http://www.qiushibaike.com/8hr/page/'

url='http://www.qiushibaike.com/'
r=requests.get(url).text
soup=BeautifulSoup(r,'html.parser')
i=soup.find_all('div',{'class':'content'})
for span in i:
    xiaohua=span.contents[1].get_text()
    xiaohua_text=xiaohua+'\n'
    print (xiaohua_text)






