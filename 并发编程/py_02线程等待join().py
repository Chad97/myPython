import threading


# 定义action函数准备作为线程执行体使用
def action(max):
    for i in range(max):
        print(threading.current_thread().name + " " + str(i))


# 启动子线程
threading.Thread(target=action, args=(10,), name="新线程").start()
for i in range(100):
    if i == 20:
        jt = threading.Thread(target=action, args=(20,), name="被Join的线程")
        jt.start()
        # 主线程调用了jt线程的join()方法，主线程
        # 必须等jt执行结束才会向下执行
        jt.join()
    print(threading.current_thread().name + " " + str(i))


"""
上面程序中一共有三个线程，主程序开始时就启动了名为“新线程”的子线程，该子线程将会和主线程并发执行。当主线程的循环变量 i 等于 20 时，启动了名为“被Join的线程”的线程，该线程不会和主线程并发执行，主线程必须等该线程执行结束后才可以向下执行。

"""