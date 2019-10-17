import time
import tkinter
import tkinter.messagebox
from threading import Thread


"""
在一个界面中，有“下载”和“关于”两个按钮，如果不用多线程技术的话，
当点击下载时，整个程序的其他部分就被阻塞，无法执行
"""


def main_without_thread():

    def download():
        # 模拟下载任务需要花费10秒时间
        time.sleep((3))
        tkinter.messagebox.showinfo('提示', '下载完成!')

    def showabout():
        tkinter.messagebox.showinfo('关于', '作者：Knight(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于',command=showabout)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


def main_with_thread():

    class DownloadTaskHandler(Thread):

        def run(self):
            time.sleep(3)
            tkinter.messagebox.showinfo('提示', '下载完成！')
            # 启用下载按钮
            button1.config(state=tkinter.NORMAL)

    def download():
        # 禁用下载按钮
        button1.config(state=tkinter.DISABLED)
        # 通过daemon参数将线程设置为守护线程（主程序退出就不再保留执行）
        # 在线程中处理耗时间的下载人物
        DownloadTaskHandler(daemon=True).start()

    def showabout():
        tkinter.messagebox.showinfo('关于', '作者：Knight(v1.0)')

    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)

    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=showabout)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


if __name__ == '__main__':
    main_without_thread()
    main_with_thread()