# excel_w.py

# 导入 xlwt 库
import xlwt
import json
from xlutils.copy import copy
from xlrd import *

# index: 0 1 2 3
      # 0-15 15-30 

def writeExcel(pageNum, results):
    new_results = json.loads(json.dumps(results))
    # print('--', new_results)
    # 创建 xls 文件对象
    wb = xlwt.Workbook()

    # 新增两个表单页
    sh1 = wb.add_sheet('名单')

    # 然后按照位置来添加数据,第一个参数是行，第二个参数是列
    # 写入第一个sheet
    # 序号	统一社会信用代码	组织名称 成立时间 登记管理机关
    sh1.write(0, 0, '序号')
    sh1.write(0, 1, '统一社会信用代码')
    sh1.write(0, 2, '组织名称')
    sh1.write(0, 3, '成立时间')
    sh1.write(0, 4, '登记管理机关')

    if pageNum % 2:
        print('序列book2')
        print(pageNum)
        w2 = copy(open_workbook('book1.xls'))
        for index in range(len(new_results)):
            lineX = (pageNum - 1) * 15 + (index + 1)
            w2.get_sheet(0).write(lineX, 0, new_results[index]['index'])
            w2.get_sheet(0).write(lineX, 1, new_results[index]['href'])
            w2.get_sheet(0).write(lineX, 2, new_results[index]['name'])
            w2.get_sheet(0).write(lineX, 3, new_results[index]['date'])
            w2.get_sheet(0).write(lineX, 4, new_results[index]['address'])
        w2.save('book2.xls')
    else:
        print('序列序列book1')
        print(pageNum)
        w1 = copy(open_workbook('book2.xls'))
        for index in range(len(new_results)):
            lineX = (pageNum - 1) * 15 + (index + 1)
            w1.get_sheet(0).write(lineX, 0, new_results[index]['index'])
            w1.get_sheet(0).write(lineX, 1, new_results[index]['href'])
            w1.get_sheet(0).write(lineX, 2, new_results[index]['name'])
            w1.get_sheet(0).write(lineX, 3, new_results[index]['date'])
            w1.get_sheet(0).write(lineX, 4, new_results[index]['address'])

        # 最后保存文件即可
        w1.save('book1.xls')