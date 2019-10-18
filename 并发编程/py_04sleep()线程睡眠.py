import time
for i in range(10):
    print("当前时间: %s" % time.ctime())
    # 调用sleep()函数让当前线程暂停1s
    # time.sleep(1)

# 上面程序将当前执行的线程暂停 1s。运行上面的程序，将看到程序依次输出 10 个字符串，输出两个字符串的时间间隔为 1s。