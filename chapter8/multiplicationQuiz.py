import pyinputplus as pyip
import random, time
numbersOfQuestions = 10
correctAnswers = 0
for questionNumber in range(numbersOfQuestions):
    # 生成两个随机数
    num1 = random.randint(0,9)
    num2 = random.randint(0,9)
    prompt = '#%s: %s x %s = ' % (questionNumber + 1, num1, num2)
    try:
        # 正确答案由allowRegexes传入
        # 错误答案由blockRegexes传入，并有报错提示
        pyip.inputStr(prompt, allowRegexes=['^%s$' %(num1 * num2)],
                      blockRegexes=['.*','Incorrect!'],
                      timeout=8,limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        # 如果try模块中没有捕获到异常
        print('Correct!')
        correctAnswers += 1
        time.sleep(1)
print('Score: %s / %s' % (correctAnswers,numbersOfQuestions))