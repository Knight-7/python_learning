"""
多线程程序如果没有竞争资源处理起来通常也比较简单
当多个线程竞争临界资源的时候如果缺少必要的保护措施就会导致数据错乱
临界资源：就是被多个线程竞争的资源
多线程程序有GIL问题，接受网站：https://www.jianshu.com/p/fb81d5570f05
"""
import time
import threading

from concurrent.futures import ThreadPoolExecutor


class Account(object):
    """银行账户"""

    def __init__(self):
        self.balance = 0.0
        self.lock = threading.Lock()

    def depos(self, money):
        # 通过锁保护临界资源
        with self.lock:
            new_balance = self.balance + money
            time.sleep(0.001)
            self.balance = new_balance


class AddMoneyThread(threading.Thread):
    """自定义线程类"""

    def __init__(self, account, money):
        super().__init__()
        self.account = account
        self.money = money

    def run(self):
        self.account.depos(self.money)


def main():
    account = Account()
    pool = ThreadPoolExecutor(max_workers=10)
    futures = []
    for _ in range(100):
        # 创建线程的第一种方式：
        # t = threading.Thread(target=account.depos, args=(1, ))
        # t.start() # 线程进入就绪状态
        # futures.append(t)

        # 创建线程的第二种方式：
        # tmp = AddMoneyThread(account, 1)
        # tmp.start() # 线程进入就绪状态
        # futures.append(tmp)

        # 创建线程的第三种方式：
        # 调用线程池中的线程来执行特定任务
        # 通过submit函数提交执行的函数到线程池中，submit函数立即返回，不阻塞
        # submit函数返回一个Future对象
        future = pool.submit(account.depos, 1)
        futures.append(future)
    # 关闭线程池
    pool.shutdown()
    for future in futures:
        # future.join() # 线程进入运行状态(第一、二种方法)
        future.result() # 第三种方法，result方法可以获取task的执行结果
    print(account.balance)


if __name__ == '__main__':
    main()