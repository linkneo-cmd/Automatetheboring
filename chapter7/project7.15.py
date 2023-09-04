'''
    实现任务：
    从剪切板取得文本
    找出文本中所有的电话号码和E-mail地址
    将它们粘贴到剪贴板

    代码实现：
    使用pyperclip模块复制和粘贴字符串
    创建两个正则表达式，一个匹配电话号码，一个匹配E-mail地址
    对两个正则表达式，找到所有的匹配，而不只是第一次匹配
    将匹配的字符串整理好格式放在一个字符串中，用于粘贴
    如果文本中没有找到匹配，则显示某种消息
'''

import pyperclip,re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?  # 匹配区号0次或1次，格式415或者(415)
    (\s | - | \.)?   # 匹配分割符号0次或1次，格式空格或短横线或句点
    (\d{3}) # 匹配3个号码
    (\s|-|\.)   # 匹配分割符号，格式空格或短横线或句点
    (\d{4})   # 匹配4个号码   
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # 附加条件
)''',re.VERBOSE)

# Create email regex.
emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+   # username
    @   # @ symbol
    [a-zA-Z0-9.-]+  # domain name
    (\.[a-zA-Z]{2,4})   # dot-something
)''',re.VERBOSE)

# Find matches in clipboard text.
# 分组0匹配整个表达式，所以元祖索引0处的分组就是我们感兴趣的内容
text = str(pyperclip.paste())
matches = []    # 将所有的匹配保存在列表变量中
for groups in phoneRegex.findall(text): # 程序可以“检测”几种不同的形式的电话号码，但我们希望添加的电话号码是唯一的、标准的格式，所以这里来做拼接
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text): # 将每次匹配的分组0添加到列表中
    matches.append(groups[0])

# Copy results to the clipboard
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))  # pyperclip.copy()函数只接收一个字符串值，而不是字符串的列表，因此需要在matches上调用join()方法
    print('Copied to clipboard:')
    print('\n'.join(matches))
else:
    print("No phone numbers or email addresses found.")

# 复制test.txt中的内容到剪切板，运行后输出结果
''' 
Copied to clipboard:
-010-4093
800-420-7240
415-863-9900
415-863-9950
support@nostarch.com
academic@nostarch.com
sales@nostarch.com
conferences@nostarch.com
errata@nostarch.com
info@nostarch.com
media@nostarch.com
editors@nostarch.com
rights@nostarch.com
support@nostarch.com
'''

print('try2')
allnumberandxiaoxie = re.compile(r'[0-9a-z]+')
ao = allnumberandxiaoxie.search('asdifuhouwqehcshni9736423JSKH')
print(ao.group())

print('匹配金额')
re.compile(r'^\d{1,3}(,{3})*$')
print('匹配句子')
name = re.compile(r'(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseablls)\.',re.IGNORECASE)
no = name.search('Bob eatS Apples.')
print(no.group())