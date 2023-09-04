# Automatetheboring
## 繁琐工作自动化学习笔记
第七章 模式匹配与正则表达式
第一次上传含7.1-7.4

## 在IDE里面，commond + K 提交并推送即可更新到Github上

## 注意re.compile()方法里面，带不带r是有区别的
https://blog.csdn.net/DongChengRong/article/details/78024340
个人理解不一定对，涉及到有转译符的，最好都带上r

## 9月2日 星期六
### 不区分大小写匹配
re.IGNORECASE
### sub()方法替换字符串
理解这句话：“在替换中输入分组1、2、3的文本”
sub()方法返回的就是替换完成后的字符串
### 管理复杂的正则表达式
re.VERBOSE作为第二参数
re.compile(r.''' ''')可以将正则表达式定义在多行中，更有可读性

## 逐渐变成杂乱笔记......
### 解决git推送失败问题
https://devpress.csdn.net/cloud-native/64f05117e0aa6850f5a200b4.html?dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MzQ1NDg1MSwiZXhwIjoxNjk0NDQyNjU4LCJpYXQiOjE2OTM4Mzc4NTgsInVzZXJuYW1lIjoid2VpeGluXzQ1OTM2MTI5In0.cV4l38KgUKk1tni-cRPafDo5OktHWWaNjgOMm_-lqR0

针对问题：
git报错fatal: unable to access ‘https://github.com/.../.git‘:Recv failure Connection was reset