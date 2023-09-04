import re

dayRegex = re.compile(r'(^(([0-3][1-9])|([1-9])|([1-3]0))/(([0-1][1-9])|[1-9]|10)/([1-2][0-9]{3})$)')
text1 = input('请输入DD/MM/YYYY格式的日期：（日期的范围是01—31，月份的范围是01-12，年份的范围是1000-2999）')
formatdayRegex = re.compile(r'^(\d)/')  # 如果日期是一位数字，在日期前自动加零。
text2 = formatdayRegex.sub(r'0\1/', text1)
formatmonthRegex = re.compile(r'/(\d)/')  # 如果月份是一位数字，在月份前自动加零。
text3 = formatmonthRegex.sub(r'/0\1/', text2)
mo = dayRegex.search(text3)


def dateCheck(day):
    lst = day.split('/')
    day = int(lst[0])
    month = int(lst[1])
    year = int(lst[2])
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):  # 闰年
        if month == 2 and day > 29:
            print('请输入正确的日期。')
        elif (month == 4 or 6 or 9 or 11) and day > 30:
            print('请输入正确的日期。')
        else:
            print('日期正确。')
    else:  # 不是闰年
        if month == 2 and day > 28:
            print('请输入正确的日期。')
        elif (month == 4 or 6 or 9 or 11) and day > 30:
            print('请输入正确的日期。')
        else:
            print('日期正确。')


if mo is None:
    print('请按照日期格式输入。（日期的范围是01—31，月份的范围是01-12，年份的范围是1000-2999)')
else:
    print(mo.group())
    date = mo.group()
    dateCheck(date)
