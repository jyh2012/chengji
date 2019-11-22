from urllib import request
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

def main():

    category = input("请输入查询专业代码:") 
    datas = []
    urls = ["http://yanzhao.bjut.edu.cn/ggl/2017321/14900855888739306_1.html", \
            "http://yanzhao.bjut.edu.cn/ggl/2018323/15217845216796468_1.html", \
            "http://yanzhao.bjut.edu.cn/ggl/2019320/15530203802448785_1.html" ]
    for url in urls:        
        req = request.Request(url, headers = {"User-Agent": "Mozilla/5.0"})
        response = request.urlopen(req)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        body = soup.find("body")
        headings = [tr for tr in body.find_all("tr")]
        for tr in headings:
            tds = tr.find_all("td")
            if len(tds)  == 11:  
                temp_data = []
                temp_flag = False
                for temp in range(1,len(tds)):
                    if tds[temp].get_text() == str(category):
                        temp_flag = True
                    temp_data.append(tds[temp].get_text())
                if temp_flag:
                    datas.append(temp_data)
        datas.append([])  
    list1 = datas
    data = pd.DataFrame(data = list1)
    data.to_csv(str(category)+ ".csv", encoding='utf_8_sig')
    #headings = [tr for tr in body.find_all("tr")]
    

if __name__ == '__main__':
    main()