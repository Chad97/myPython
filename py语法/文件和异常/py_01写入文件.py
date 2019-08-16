filename = 'programming.txt'
"""
定读取模式 （'r' ）、写入模式 （'w' ）、附加模式 （'a' ）或让你能够读取和写入文件的模式（'r+' ）。如果你省略了模式实参，Python将以默认的只读模式打
开文件。
"""
with open(filename, 'w') as file_obj:
    file_obj.write("i love programming .\n")
    file_obj.write("i love python .\n")

with open(filename, 'a') as file_obj:
    file_obj.write('i love life .\n')
    file_obj.write('i love music .\n')

"""
0. 访客 ：编写一个程序，提示用户输入其名字；用户作出响应后，将其名字写入到文件guest.txt中。
1. 访客名单 ：编写一个while 循环，提示用户输入其名字。用户输入其名字后，在屏幕上打印一句问候语，并将一条访问记录添加到文件guest_book.txt中。确保这个文件中的每条记录都独占一行。
2. 关于编程的调查 ：编写一个while 循环，询问用户为何喜欢编程。每当用户输入一个原因后，都将其添加到一个存储所有原因的文件中。
"""


def add_guest():
    guest = input("请输入客人姓名：")
    with open('guest.txt', 'a') as file_obj:
        file_obj.write('姓名：%s\n' % guest)


def likecode_why():
    while True:
        reason = input('你为喜欢编程的原因是什么？')
        with open('all_reason.txt', 'a') as file_obj:
            file_obj.write(reason + '\n')


likecode_why()