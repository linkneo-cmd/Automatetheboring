'''
    日期检测
    便携一个正则表达式，可以检测DD/MM/YYYY格式的日期
    假设日期的范围是01～31，月份的范围是01～12，年份的范围是1000～2999
    如果日期或月份是一位数字，会在前面自动加0

    不必检测每个月或闰年的正确日期
    将字符串存储到month，day，year的变量中
'''

import re

date = re.compile(r'''(
    (\d{1,2})  # day
    \\
    (\d{1,2})   # month
    \\
    (\d{4}) # year
)''',re.VERBOSE)
dates = '01\01\1999 12\\31\\2000 2\\28\\2013 123\\21\\3456'
days = []    # 将所有的匹配保存在列表变量中
months = []
years = []
for groups in date.findall(dates): # 程序可以“检测”几种不同的形式的电话号码，但我们希望添加的电话号码是唯一的、标准的格式，所以这里来做拼接
    days.append(groups[0])
    months.append(groups[0])
    years.append(groups[0])

print('\n'.join(days))
