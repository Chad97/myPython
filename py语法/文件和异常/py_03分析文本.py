def count_words(filename):
    """ 计算一本书包含多少个单词 """
    try:
        with open(filename, 'rb') as f:
            contents = f.read()
    except FileNotFoundError:
        print('抱歉没有这个文件')
    else:
        #  计算大致包含多少个单词
        words = contents.split()
        print('文件 %s 包含 %s 个单词' % (filename, len(words)))


filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']

for name in filenames:
    count_words(name)
else:
    print('\n分析完毕')