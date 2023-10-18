'''
    该程序利用一个关键字保存每段剪贴板文本。
    例如，当运行py mcb.pyw save pam时
    剪贴板中当前的内容就用关键字spam保存。运行py mcb.pyw spam，这段文本稍后将重新家在到剪贴板中。
    如果用户忘记了都有哪些关键字，可以运行py mcb.pyw list ，将所有关键字的列表复制到剪贴板中。

    1、从sys.argv读取命令行参数
    2、读写剪贴板
    3、保存并加载shelf文件
'''

import shelve, pyperclip, sys
mcbShelf = shelve.open('mcb')
# Save clipboard content
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
    # List keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
mcbShelf.close()