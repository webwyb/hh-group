import requests;
import json;
import bs4;
from bs4 import BeautifulSoup;
from writeExcel import writeExcel;

# results = [{'index': '1', 'href': '/biz/ma/csmh/a/csmhadetail.html?aaee0101=ff8080816f339642016f7df2cf9b1090', 'name': '南京市圆梦青少年发展基金会\r\n\t\t\t\t\t', 'date': '2019-5-6', 'address': '南京市民政局'}, {'index': '2', 'href': '/biz/ma/csmh/a/csmhadetail.html?aaee0101=ff8080816f339642016f7df62bd61093', 'name': '南京秦淮河文化旅游基金会\r\n\t\t\t\t\t', 'date': '2019-7-5', 'address': '南京市民政局'}, {'index': '3', 'href': '/biz/ma/csmh/a/csmhadetail.html?aaee0101=ff80808173268cc2017326d54b770054', 'name': '新余市扶贫慈善基金会\r\n\t\t\t\t\t', 'date': '2019-6-11', 'address': '新余市民政局'}, {'index': '4', 'href': '/biz/ma/csmh/a/csmhadetail.html?aaee0101=ff80808173268cc20173280837a6013a', 'name': '牟定县红十字会\r\n\t\t\t\t\t', 'date': '1999-7-1', 'address': '牟定县机构编制办公室'}]
# results = []
# 获取html文档
def getHtml(pageNum):
    url = 'http://cishan.chinanpo.gov.cn/biz/ma/csmh/a/csmhaDoSort.html?aaee0102_03=&field=aaex0131&sort=desc&flag=0'
    From_data = {
        'pageNo': pageNum
    }
    # 请求数据
    responses = requests.post(url, data=From_data)
    strhtml = responses.text;
    soup = BeautifulSoup(strhtml, features="html.parser")
    return soup;

# 从html获取数据
def getDataFromHtml(html):
    results = []
    tables = html.findAll('table')
    tab = tables[0]
    for tr in tab.tbody.findAll('tr'):
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            result = {
                'index': tds[0].string,
                'code': tds[1].string,
                'href': tds[2].a.get('href'),
                'name': tds[2].a.get_text(),
                'date': tds[3].string,
                'address': tds[4].string,
            }
            results.append(result);
    return results;
# 写入Excel
def writeDataToExcel(index,results):
    writeExcel(index,results)

# getHtml(2)
for i in range(1,100):
    htmlStr = getHtml(i)
    results = getDataFromHtml(htmlStr)
    # print('***',results)
    writeDataToExcel(i, results)
