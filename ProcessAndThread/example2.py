from time import time
from multiprocessing import Process, Queue


"""
采用分而治之的思想
"""


def calculate_without_precess():
    total = 0
    number_list = [x for x in range(1, 100000001)]
    start = time()
    for number in number_list:
        total += number
    print(total)
    end = time()
    print('总共耗时%.2f秒' % (end - start))


def calculate_with_process():

    def task_handler(curr_list, result_queue):
        total = 0
        for number in curr_list:
            total +=  number
        result_queue.put(total)

    def main():
        processes = []
        number_list = [x for x in range(1, 100000001)]
        result_queue = Queue()
        index = 0
        # 启动8个进程将数据切片后进行运算
        for _ in range(8):
            p = Process(target=task_handler, args=(number_list[index: index + 12500000], result_queue))
            processes.append(p)
            index += 12500000
            p.start()
            # 开始记录所有进程执行完成花费的时间
        start = time()
        for p in processes:
            p.join()
        total = 0
        while not result_queue.empty():
            total += result_queue.get()
        print(total)
        end = time()
        print('总共耗时%.2f秒' % (end - start))

    main()


if __name__ == '__main__':
    calculate_without_precess()
    calculate_with_process()
