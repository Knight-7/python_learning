from random import randint
from time import time, sleep
from threading import Thread


"""
Python中的多线程
"""


# 多线程
def with_thread():
    def download(filename):
        print('开始下载%s'%(filename))
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成，耗时：%d秒'%(filename, time_to_download))

    def download_main():
        start = time()
        # 通过Thread创建一个线程
        t1 = Thread(target=download, args=('Python入门到住院.pdf',))
        t2 = Thread(target=download, args=('Peking Hot.avi',))
        # 通过start方法开始线程
        t1.start()
        t2.start()
        # 通过join方法等等待线程执行结束
        t1.join()
        t2.join()
        end = time()
        print('总共耗费了%.f秒'%(end - start))

    download_main()


# 自己创建一个继承Thread的类
class DownloadTask(Thread):
    """一个继承线程的下载任务类"""
    def __init__(self, filename):
        super().__init__()
        self._filename = filename

    def run(self):
        print('开始下载%s'%(self._filename))
        time_to_download = randint(5, 10)
        sleep(time_to_download)
        print('%s下载完成！耗费了%d秒'%(self._filename, time_to_download))


def down_with_class():
    start = time()
    c1 = DownloadTask('Python从入门到住院.pdf')
    c2 = DownloadTask('Peking Hot.avi')
    c1.start()
    c2.start()
    c1.join()
    c2.join()
    end = time()
    print('总共耗费%.2f秒'%(end - start))


if __name__ == '__main__':
    with_thread()
    down_with_class()