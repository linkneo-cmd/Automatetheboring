# isPhoneNumber()函数进行了几项检查，任何一项检查不通过就返回False
# 检查是否12位
# 检查前3个是否只包含了数字
# 检查第四个元素是不是短横线
# 接下来3个数字
# 又跟一个短横线
# 最后4位数字

def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0, 3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4, 7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(8, 12):
        if not text[i].isdecimal():
            return False
    return True

print('415-555-4242 is a phone number:')
print(isPhoneNumber('415-555-4242'))
print('Moshi Moshi is a phone number')
print(isPhoneNumber('Moshi moshi'))

# 替换上面的4个print
# for循环的每一次迭代中，去message的一段新的12个字符赋给变量chunk
message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('phone number found: ' + chunk)
print('Done')

# python中所有正则表达式的函数都在re模块中
# \d是一个正则表达式，表示一位数字字符，即任何一位0～9的数字
# \d\d\d-\d\d\d-\d\d\d\d可以匹配前面isPhoneNumber（）同样的文本
# {3}表示匹配三次
# \d{3}-\d{3}-\d{4}效果一样

import re
# phoneNumbergex变量包含了一个Regex对象
# Regex对象的serch()方法查找传入的字符串
# 没找到返回None
# 找到了返回一个Match对象
# Match对象有一个group方法，返回实际匹配的文本
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone Number found: ' + mo.group())

print('利用括号分组：')
# 第一对括号是第一组，第二对括号是第二组
# 向group传入整数1或2，可以匹配不同的部分
# 传入0或者不传入参数，返回整个匹配文本
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
# 一次获得所有分组，使用groups()
print('使用groups()')
print(mo.groups())
areaCode, mainNumber = mo.groups()
print(areaCode)
print(mainNumber)

# 如果需要匹配括号，需要对括号进行转译
phoneNumRegex = re.compile(r'(\(\d\d\d\))(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My phone number is (415)555-4242.')
print(mo.group(1))
print(mo.group(2))

# 这些字符都具有特殊含义. ^ $ * + ? { } [ ] \ | ( )

print('用管道匹配多个分组')
heroRegex = re.compile(r'Batman|Tina Fey')
mo1 = heroRegex.search('Batman and Tian Fey')
# 如果Batman和Tina Fey都出现在被查找的字符串中，第一次出现的匹配文本会将作为match对象返回
print(mo1.group())
mo2 = heroRegex.search('Tina Fey and Batman')
print(mo2.group())

# 使用管道匹配多个模式中的任意一个，比如希望匹配Batman、Batmobile、Batcopter、Batbat中的任意一个
print('使用管道匹配多个模式中的任意一个')
batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batmobile list a wheel')
print(mo.group())
print(mo.group(1))

# 用问号实现可选匹配
# 想匹配的模式是可选的，(wo)?表示是可选的分组，在匹配的文本中，wo将出现零次或一次
batRegex = re.compile(r'Bat(wo)?man')
mo1 = batRegex.search('The adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The adventures of Batwoman')
print(mo2.group())

# 让正则表达式寻找包含区号和不包含区号的电话号码
phoneRegex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phoneRegex.search('My number is 415-555-4242')
print(mo1.group())
mo2 = phoneRegex.search('My number is 555-4242')
print(mo2.group())

# 用星号匹配零次或多次
# 星号之前的分组可以在文本出现任意次，也可以完全不存在，也可以一次又一次重复
print('用星号匹配零次或多次')
batRegex = re.compile(r'Bat(wo)*man')
mo1 = batRegex.search('The Adventures of Batman')
print(mo1.group())
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())

# group用加号匹配一次或多次
# 注意区别，加号是一次或多次，星号是零次或多次
# 加号要求wo至少出现一次，所以mo1是None
print('用加号匹配一次或多次')
batRegex = re.compile(r'Bat(wo)+man')
mo2 = batRegex.search('The Adventures of Batwoman')
print(mo2.group())
mo3 = batRegex.search('The Adventures of Batwowowowoman')
print(mo3.group())
mo1 = batRegex.search('The Adventures of Batman')
print(mo1)

# 用花括号匹配特定次数
# (Ha){3}会匹配字符串'HaHaHa'，但不会匹配'HaHa'，因为后者只重复了(Ha)分组两次
# 还可以指定一个范围(Ha){3, 5}将匹配'HaHaHa'、'HaHaHaHa'、'HaHaHaHaHa'
# 也可以不写花括号里第一个或者第二个数字，表示不限定最小值或者最大值
# (Ha){3, }表示3次或者更多次
# (Ha){,5}表示0～5次
# 一些等价的表达：
# (Ha){3}
# (Ha)(Ha)(Ha)
# (Ha){3,5}
# ((Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha))|((Ha)(Ha)(Ha)(Ha)(Ha))
print('用花括号匹配特定次数')
haRegex = re.compile(r'(Ha){3}')
mo1 = haRegex.search('HaHaHa')
print(mo1.group())
mo2 = haRegex.search('Ha')
print(mo2)

# 贪心和非贪心匹配
# python的正则表达式默认是贪心的，在有二义的前提下，会尽可能匹配最长的字符串
# 如果在结束的花括号后面加一个问号，就非贪心的，会尽可能匹配最短的字符串
# 问号现在在正则表达式中可能有两种含义了，一种是声明非贪心匹配，一种是表示可选的分组
print('贪心和非贪心匹配')
greedyHaRegex = re.compile(r'(Ha){3,5}')
mo1 = greedyHaRegex.search('HaHaHaHaHa')
print(mo1.group())
nongreedyHaRegex = re.compile(r'(Ha){3,5}?')
mo2 = nongreedyHaRegex.search('HaHaHaHaHa')
print(mo2.group())

# 新增一条备注，验证github上传情况

# findall()方法
# 返回一组字符串，包含被查找字符串中所有匹配的文本
print("findall()方法")
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('Cell:415-555-9999 Work:212-555-0000')
print(mo.group())
print('没有分组的情况')
# 返回一个字符串列表
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.findall('Cell:415-555-9999 Work:212-555-0000')
print(mo)
print('有分组的情况')
# 返回一个元祖列表
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo = phoneNumRegex.findall('Cell:415-555-9999 Work:212-555-0000')
print(mo)

# something changed here...