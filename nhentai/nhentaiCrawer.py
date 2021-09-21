import bs4
from bs4 import BeautifulSoup
import requests

def crawler(number,page):
    urls = []
    page = 0
    while 1:
        print(f"第{page+1}頁爬蟲")
        url = f"https://nhentai.net/g/{number}/{page+1}/"
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362'}
        r = requests.get(url,headers=headers)
        Burl = BeautifulSoup(r.text, 'html.parser')
        img_tags = Burl.find_all('img')
        for tag in img_tags:
            imgUrl = tag.get('src')
        print(f"imgUrl: {imgUrl}")
        if imgUrl == "https://static.nhentai.net/img/logo.090da3be7b51.svg":
            break
        urls.append(imgUrl)
        page += 1
    return urls,url