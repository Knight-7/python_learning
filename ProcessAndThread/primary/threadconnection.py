from threading import Thread, Lock
from time import sleep


""""
线程之间的通信
"""


class AccountWithoutLock(object):

    def __init__(self):
        self._balance = 0

    def deposit(self, money):
        new_balance = self._balance + money
        sleep(0.01)
        self._balance = new_balance

    @property
    def balance(self):
        return self._balance


class AccountWithLock():

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        # 获取锁才能执行后续代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证异常都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(Thread):

    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def with_no_lock():
    account = AccountWithoutLock()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # join 方法表示等待线程执行结束
    for t in threads:
        t.join()
    print('账户余额为：￥%d元' % account.balance)
    """结果为1，因为在每个进程运行到new_balance = self._balance + money时，self._balance的值
    还是0，（因为sleep(0.5),此时进程还没运行到self._balance = new_balance,所以self._balance还是0）
    所以最终的结果为1
    """


def with_lock():
    account = AccountWithLock()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    # join()方法表示等待所有的线程结束再运行后面的代码，如果不加的话，
    # 那么线程的函数还在运行，但是已经开始执行后面的print函数了，那么
    # 这时候的结果就是还没有完全加完的
    for t in threads:
        t.join()
    print('账户余额为：￥%d元' % account.balance)


if __name__ == '__main__':
    # with_no_lock()
    with_lock()