import requests,bs4
from bs4 import BeautifulSoup
import os


'''
爬取机核网文章
'''

url = "https://www.gcores.com/articles/114335"
header = {
    'Host':'www.gcores.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'
    }

re = requests.get(url,headers=header).text
#print(re)

soup = BeautifulSoup(re, "lxml")
#print(soup)

find_a = soup.find('title').get_text() #文章标题
#print(type(find_a))

for i in soup.find_all('span',attrs={"data-text":"true"}): #正文内容
    print(i.get_text())





