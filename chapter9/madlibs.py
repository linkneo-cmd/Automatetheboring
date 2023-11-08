'''
    首先命令行会打印madlibs.txt中的一行话，接着提示可以替换里面的大写字母的词
    替换后生成一句新的话，打印出来，并添加到madlib_new.txt文件中
'''

import re

file = open('./madlibs.txt', 'r')
content = file.read()
print(content)
mad_lib_words = list(content.split())
file.close()

adj_regex = re.compile(r'ADJECTIVE')
noun_regex = re.compile(r'NOUN')
adv_regex = re.compile(r'ADVERB')
verb_regex = re.compile(r'VERB')

result_file = open('./madlibs_new.txt', 'a')
result_string = ""
for word in mad_lib_words:
    if adj_regex.match(word):
        word = adj_regex.sub(input("Give an adjective: "), word)
    elif noun_regex.match(word):
        word = noun_regex.sub(input("Give a noun: "), word)
    elif verb_regex.match(word):
        word = verb_regex.sub(input("Give a verb: "), word)
    elif adv_regex.match(word):
        word = adv_regex.sub(input("Give a adverb: "), word)
    result_string += word + " "
result_file.write(result_string + "\n")

print(result_string)
result_file.close()