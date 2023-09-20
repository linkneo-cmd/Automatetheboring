'''
    编写一个程序，向用户询问他们的三明治偏好。程序应使PyInputPlus来确保有效的输入
    面包类型使用inputMenu():wheat、white、sourdough
    对蛋白质类型使用inputMenu():chicken、turkey、ham或tofu
    用inputYesNo()询问他们是否要cheese
    如果需要cheese，请使用inputMenu()询问cheese类型：cheddar、Swiss或mozzarella
    用inputYesNo询问他们是否需要mayo、mustard、lettuce或tomato
    用inputInt()询问他们想要多少个三明治。确保这个数字为1或更大
    列出每个选项的的价格，并在用户输入选择后让程序显示总费用
'''

# '''
#     伪代码：
#     Num = inputInt()，需要多少个三明治
#     for i in range Num，一个个遍历询问
#     {
#         char1 = inputMenu()
#         amt1 =
#         char2 = inputMenu()
#         amt2 =
#         CheeseResponse = inputYesNo('你需要奶酪么？(y\\n)')
#         amt3 = 0
#         char3 = ''
#         if(CheeseResponse == 'yes')
#         {
#             char3 = inputMenu()
#             amt3 =
#         }
#         VegetableResponse = inputYesNo('你需要蔬菜么？(y\\n)')
#         amt4 = 0
#         char4 = ''
#         if(VegetableResponse == 'yes')
#         {
#             char4 = inputMenu()
#             amt4 =
#         }
#         sum = amt1 + amt2 + amt3 + amt4
#     }
#     priceList[i] = int()
# '''
import pyinputplus as pyip, re

menu = [{'wheat': '5.5 ¥', 'white': '6.5 ¥', 'sourdough': '7.5 ¥'},
        {'chicken': '2.5 ¥', 'turkey': '3.4 ¥', 'ham': '2.4 ¥', 'tofu': '3.3 ¥'},
        {'cheddar': '3.5 ¥', 'Swiss': '2.7 ¥', 'mozzarella': '5.1 ¥'},
        {'mayo': '4.5 ¥', 'mustard': '7.2 ¥', 'mayo & mustard': '5.8 ¥'},
        {'lettuce': '6.5 ¥', 'tomato': '7.1 ¥', 'lettuce & tomato': '8.3 ¥'}]

menuText = ['输入面包类型:',
            '输入蛋白质类型:',
            '你需要奶酪么?(y/n)',
            '你需要酱么?(y/n)',
            '你需要蔬菜么?(y/n)',
            '你需要几个三明治?:']

order = []
totalCost = 0


def pyIP(text, choice, yn):
    if text:
        print(text)
    if yn == True:
        return pyip.inputYesNo(prompt='')
    elif yn == False:
        return pyip.inputMenu(
            [k + ' ' + v for k, v in menu[choice].items()],
            numbered=True, prompt='') # numbered = True会显示选项1、2、3...，并且可以通过输入1、2、3来进行选择
    elif yn == 'end':
        return pyip.inputInt(min=1, prompt='') # 至少得要一个

for i in range(len(menuText)):
    if i <= 1:
        order.append(pyIP(menuText[i], i, False))
    elif i in range(2, 5):
        if pyIP(menuText[i], i, True) == 'yes':
            order.append(pyIP('', i, False))
    elif i == 5:
        totalSandwiches = pyIP(menuText[i], i, 'end')

for i in [re.sub(r'[^0-9.]', '', i) for i in order]: # 匹配除了0-9和.之外的所有字段，并且将这些字段替换为空
    totalCost += float(i) * totalSandwiches

print(f'Total price: {round(totalCost, 2)} ¥')