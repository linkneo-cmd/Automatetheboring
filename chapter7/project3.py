'''
    strip()的正则表达式版本
    写一个字符串，它接收一个字符串，做的事情和strip()字符串方法一样。
    如果只传入了要去除的字符串，没有其他参数，那么就从该字符串的首尾去除空白字符；
    否则，函数第二个参数指定的字符将从该字符串中去除
'''

import re

str1 = input('请输入原字符串：')
str2 = input('请输入原字符串中要删除的字符：')

def newstrip(str1,str2):
    strRegex1 = re.compile(r'^\s+|\s+$')
    strRegex2 = re.compile(str2)
    if str2 == '':
        temp = strRegex1.sub('',str1)   #替换空格
        print("1")
    else:
        temp = strRegex2.sub('',str1)   #替换指定的字符
        print("2" + str2 + "2")
    print(temp)

newstrip(str1,str2)