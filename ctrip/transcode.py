#-*- coding:utf-8 -*-
import sys
import os
reload(sys)
sys.setdefaultencoding('utf-8')

with open('out.csv','r') as input_file, open('out_gbk.csv', 'w') as output_file:
    lines = input_file.readlines()
    for line in lines:
        try:
            print >> output_file, line.strip().replace(';',' ').replace('&nbsp',' ').replace('\r','').replace('\n','').encode('gbk')
        except:
            continue