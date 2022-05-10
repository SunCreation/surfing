import chromedriver_autoinstaller
from selenium import webdriver
from bs4 import BeautifulSoup

chromedriver_autoinstaller.install()
browser = webdriver.Chrome()

import time


# https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%EB%B6%80%EB%8F%99%EC%82%B0
# 주소와 파라미터(변수)로 되어있다. 
url = r'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q=%ED%8C%8C%EC%9D%B4%EB%A6%AC'

print(url)

url2 = r'http://www.q-net.or.kr/crf005.do?id=crf00503&jmCd=1320&gSite=Q&gId='

wordlist = ['모두연','파이썬','카카오','벗꽃']

for i in wordlist:
    url = f'https://search.daum.net/search?nil_suggest=btn&w=tot&DA=SBC&q={i}'
    print(url)
    browser.get(url)
    time.sleep(10)

time.sleep(1000)