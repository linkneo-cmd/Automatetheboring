'''
Write a program that asks users for their sandwich preferences. The pro-
gram should use PyInputPlus to ensure that they enter valid input, such as:
•	 Using inputMenu() for a bread type: wheat, white, or sourdough.
•	 Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
•	 Using inputYesNo() to ask if they want cheese.
•	 If so, using inputMenu() to ask for a cheese type: cheddar, Swiss,
or mozzarella.
•	 Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
•	 Using inputInt() to ask how many sandwiches they want. Make sure this
number is 1 or more.
Come up with prices for each of these options, and have your program
display a total cost after the user enters their selection.
'''

import pyinputplus as pyip, re

menu = [{'wheat': '1.1 €', 'white': '2.4 €', 'sourdough': '3.2 €'},
        {'chicken': '1.5 €', 'turkey': '2.23 €', 'ham': '3.34 €', 'tofu': '4.34 €'},
        {'cheddar': '1.56 €', 'Swiss': '2.39 €', 'mozzarella': '3.67 €'},
        {'mayo': '0.23 €', 'mustard': '0.45 €', 'mayo & mustard': '0.59 €'},
        {'lettuce': '0.12 €', 'tomato': '0.16 €', 'lettuce & tomato': '0.23 €'}]

menuText = ['Enter a bread type:',
            'Enter a protein type:',
            'Do you want cheese?(y/n)',
            'Do you want dressing?(y/n)',
            'Do you want vegetables?(y/n)',
            'How many sandwiches do you want?:']

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
            numbered=True, prompt='')
    elif yn == 'end':
        return pyip.inputInt(min=1, prompt='')


for i in range(len(menuText)):
    if i <= 1:
        order.append(pyIP(menuText[i], i, False))
    elif i in range(2, 5):
        if pyIP(menuText[i], i, True) == 'yes':
            order.append(pyIP('', i, False))
    elif i == 5:
        totalSandwiches = pyIP(menuText[i], i, 'end')

for i in [re.sub(r'[^0-9.]', '', i) for i in order]:
    totalCost += float(i) * totalSandwiches

print(f'Total price: {round(totalCost, 2)} €')