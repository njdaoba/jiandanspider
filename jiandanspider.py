#coding=utf-8
import urllib
import urllib2
from random import random

from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options




def getPage(url):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(url)
    return driver.page_source


def downloadimg(html):
    sup = BeautifulSoup(html,'html.parser')
    for imgurl in sup.find_all(class_='view_img_link'):
        img = 'http:'+ imgurl['href']
        filename = img.split('/')[-1]
        print(img.split('/')[-1])
        urllib.urlretrieve(img, 'D:/meizi/' + filename)



base_url = "https://jandan.net/ooxx/page-"
baseurl = "#comments"
for i in range(13,0,-1):
    url = base_url+str(i)+baseurl
    print(url)
    try:
        html = getPage(url)
    except TimeoutException as t:
        print("File download:"+str(i))
    downloadimg(html)
