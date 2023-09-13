# exercise09_05.py
注意是inputCustom(addsUpToTen),而不是inputCustom(addsUpToTen())。

因为这里我们是将addsUpToTen()函数本身传递给inputCustom()，

而不是调用addsUpToTen()并传递其返回值
# busy.py
1、询问用户是否想知道如何让人忙几小时

2、如果用户回答no，退出

3、如果用户回答yes，转到步骤1

注意if判断是在while True的分支里面的
# multiplicationQuiz.py
向用户提出10个乘法问题，其中有效的出入是问题的正确答案

传入allowRegexes参数是一个列表，其中%s会被替换成正确的答案，

传入blocklistRegexes参数是一个列表。元组中的第一个字符串是与每个可能的字符串匹配的正则表达式 。

因此，如果用户的回答与正确答案不符，该程序将拒绝他们提供到的答案。

在这种情况下，将显示字符串'Incorrect!'，并提示用户再次作答

另外，传入timeout和limit，用户只有8秒和3次机会来作答

else块可以跟随if或elif，它也可以跟随一个except块

for循环的末尾放置1s的暂停时间，使用户有时间阅读消息