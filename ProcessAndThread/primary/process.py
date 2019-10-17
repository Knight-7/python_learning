from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


"""
Python中的多进程
"""


def with_no_process():
    def download_task(filename):
        print('开始下载%s。。。'%filename)
        time_to_download = randint(5,10)
        sleep(time_to_download)
        print('\n%s下载完成！耗费了%d秒。'%(filename, time_to_download))

    def download_main():
        start = time()
        download_task('Python从入门到住院.pdf')
        download_task('Peking Hot.avi')
        end = time()
        print('总共耗费了%.2f秒'%(end - start))

    download_main()


# 多进程
def with_process():
    def download_task(filename):
        print('启动下载进程，进程号[%d]'%getpid())
        print('开始开始下载%s...'%filename)
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成！耗费了%d秒'%(filename, time_to_download))

    def downlaod_main():
        start = time()
        # 通过Process类来创建进程对象，target参数传入我们传入一个函数表示进程要执行的代码，args是一个元组，代表传给函数的参数
        p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
        p2 = Process(target=download_task, args=('Peking Hot.avi', ))
        # 调用start方法启动进程
        p1.start()
        p2.start()
        # 用join方法等待进程执行结束
        p1.join()
        p2.join()
        end = time()
        print('总共耗费了%.2f秒'%(end - start))

    downlaod_main()


if __name__ == '__main__':
    # with_no_process()
    with_process()