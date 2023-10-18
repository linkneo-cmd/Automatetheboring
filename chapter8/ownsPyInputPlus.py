'''
 要想明白PyInputPlus为你做了多少事，请尝试不导入它，自己重新创建乘法测验项目。
 该程序想用户提出10个乘法问题，范围从0x0到9x9。你需要实现一下功能
 （1）如果用户输入正确的答案，程序将显示“Correct！”并停留1秒，然后转到下一个问题
 （2）程序进入下一个问题之前，用户有3次输入正确答案的机会
 （3）首次显示问题8秒后，该问题的答案将被标记为不正确，及时用户之后输入了正确的答案
'''
import random, time
numbersOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numbersOfQuestions):
    # 生成两个随机数
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    times = 0
    prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)
    print(prompt)
    starttime = 0
    while(times < 3):
        if(starttime == 0):
            starttime = time.time()
        while(True):
            answer = input()
            try:
                answer = int(answer)
                break
            except ValueError:
                print('Not a number, please try again.')
        if((answer == num1*num2) and ((time.time()-starttime) < 8)):
            print("Correct!")
            time.sleep(1)
            correctAnswers += 1
            break
        elif((time.time()-starttime)>=8):
            print('Time\'s up.')
            break
        else:
            times += 1
            if times < 3:
                print("Try again, you have " + str(3 - times) +" chances")
            else:
                print("Sorry, next one.")
            continue
print('Score: %s / %s' % (correctAnswers,numbersOfQuestions))