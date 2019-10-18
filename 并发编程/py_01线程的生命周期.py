import threading

# TODO 线程的新建和就绪状态


# 定义准备作为线程执行体的action函数
def action(max):
    for i in range(max):
        # 直接调用run()方法时，Thread的name属性返回的是该对象的名字
        # 而不是当前线程的名字
        # 使用threading.current_thread().name总是获取当前线程的名字
        print(threading.current_thread().name + " " + str(i))  # ①


for i in range(100):
    # 调用Thread的currentThread()方法获取当前线程
    print(threading.current_thread().name + " " + str(i))
    if i == 20:
        # 直接调用线程对象的run()方法
        # 系统会把线程对象当成普通对象，把run()方法当成普通方法
        # 所以下面两行代码并不会启动两个线程，而是依次执行两个run()方法
        # threading.Thread(target=action,args=(10,)).run()
        # threading.Thread(target=action,args=(10,)).run()
        pass


# TODO 线程死亡
""" 
启动过且结束了的进程，视为为死亡进程 
"""


# 定义action2函数准备作为线程执行体使用
def action2(max):
    for i in range(10):
        print(threading.current_thread().name + " " + str(i))


# 创建线程对象
sd = threading.Thread(target=action2, args=(100,))
for i in range(50):
    # 调用threading.current_thread()函数获取当前线程
    print(threading.current_thread().name + " " + str(i))
    if i == 20:
        # 启动线程
        sd.start()
        # 判断启动后线程的is_alive()值，输出True
        print(sd.is_alive())
    # 当线程处于新建、死亡两种状态时，is_alive()方法返回False
    # 当i > 20时，该线程肯定已经启动过了，如果sd.is_alive()为False时
    # 那就是死亡状态了
    if i > 20 and not(sd.is_alive()):
        # 试图再次启动该线程
        print(sd.is_alive())
        sd.start()
