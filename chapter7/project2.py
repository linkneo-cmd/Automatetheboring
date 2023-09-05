'''
    强口令检测
    写一个函数，使用正则表达式，确保传入的口令字符串是强口令。
    强口令的定义是：长度不少于8个字符，同时包含大写和小写字符，至少有一位数字
'''
import re
def check(password):
    num = len(password)
    pwRegex1 = re.compile(r'[a-z]+')
    pwRegex2 = re.compile(r'[A-Z]+')
    pwRegex3 = re.compile(r'[0-9]+')

    if pwRegex1.search(password) is None:
        print('请输入至少一个小写字母!')
    if pwRegex2.search(password) is None:
        print('请输入至少一个大写字母!')
    if pwRegex3.search(password) is None:
        print('请输入至少一个数字!')
    if num < 8:
        print('密码长度大于8!')
    if (num >= 8) and (pwRegex1.search(password) is not None) and (pwRegex2.search(password) is not None) and (pwRegex3.search(password) is not None):
        return True
while True:
    pw = input("请输入密码:")
    if check(pw) is True:
        print("Your password is:" + pw + "\nplease remember it.")
        break
