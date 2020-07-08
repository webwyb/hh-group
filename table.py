import requests
import bs4
from bs4 import BeautifulSoup
 
 
def getHTMLText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""
 
 
def fillulist(ulist, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('table', {'class': 'hq_table'}).children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[2].string, tds[3].string, tds[4].string, tds[5].string, tds[6].string])
 
 
def printlist(ulist, num):
    a = "{:^15}\t{:^15}\t{:^15}\t{:^15}\t{:^15}\t{:^15}\t{:^15}"
    print(a.format("品名", "最低价", "平均价", "最高价", "规格", "单位", "发布日期"))
    for i in range(num):
        u = ulist[i]
        print(a.format(u[0],u[1], u[2], u[3], u[4], u[5], u[6]))
 
 
def main():
    unifo = []
    url = "http://www.xinfadi.com.cn/marketanalysis/0/list/1.shtml"
    html = getHTMLText(url)
    fillulist(unifo, html)
    printlist(unifo, 20)
main()