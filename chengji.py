from urllib import request
from bs4 import BeautifulSoup
import numpy as np

def main():
    url = "http://yanzhao.bjut.edu.cn/ggl/2017321/14900855888739306_1.html"
    req = request.Request(url, headers = {"User-Agent": "Mozilla/5.0"})
    response = request.urlopen(req)
    html = response.read()
    soup = BeautifulSoup(html, 'lxml')
    table = soup.find("table")
    headings = [th.get_text() for th in table.find("tr").find_all("th")]
    print('a')

if __name__ == '__main__':
    main()