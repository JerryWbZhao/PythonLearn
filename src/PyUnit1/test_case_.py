#-*-coding=utf-8 -*-
import os
#列出某个文件夹下的所有case,这里用的是python，所在py 文件运行一次后会生成一个pyc的副本
caselist=os.listdir('D:\\selenium_use_case\\test_case')
for a in caselist:
    s=a.split('.')[1:][0] #选取所要执行的用例
    if s=='py':
        #此处执行dos 命令并将结果保存到log.txt
        os.system('D:\\selenium_use_case\\test_case\\%s 1>>log.txt 2>&1'%a)