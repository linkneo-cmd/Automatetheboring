from pathlib import Path
import pyinputplus as pyip
import re

#请输入一个匹配规则
regex = pyip.inputRegexStr('Please input a regex: ')
pattern = re.compile(regex)
#获取当前路径
p = Path.cwd()
#获取当前路径下，所有匹配.txt尾缀的文件名
for txtFlie in list(p.glob('*.txt')):
    #读这些txt文件的每一行
    with open(txtFlie) as curFile:
        txtLines = curFile.readlines()
        #如果这些行匹配到了pattern,则输出到屏幕上
        for txtLine in txtLines:
            if(pattern.search(txtLine)):
                print(txtLine)