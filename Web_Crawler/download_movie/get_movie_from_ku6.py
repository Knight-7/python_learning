import requests
import time

from threading import Thread


def print_process(p_size, size, content_size, chunk_size):
    print('已经下载了：', end='')
    print(int(size / content_size * 100) * '█', end='')
    print(f'【{round(size / chunk_size ** 2, 2)}MB】', end='')
    print(f'【{round(float(size / content_size) * 100, 2)}%】', end='')
    print(f'速度:{round(float((size - p_size) / chunk_size ** 2), 2)}MB/s')


def get_vedio():
    start = time.time()
    url = 'https://rbv01.ku6.com/wifi/o_1dlm9titl1kqj1qmp1lkb5g9vrttkvs'
    try:
        size = 0
        response = requests.get(url, stream=True)
        chunk_size = 1024
        content_size = int(response.headers['content-length'])
        print(f'文件大小{round(float(content_size / chunk_size ** 2), 2)}MB')
        with open('v1.mp3', 'wb') as f:
            s_time = time.time()
            p_size = 0
            for data in response.iter_content(chunk_size):
                f.write(data)
                size += len(data)
                if (time.time() - s_time >= 1):
                    print_process(p_size, size, content_size, chunk_size)
                    s_time = time.time()
                    p_size = size
        print_process(p_size, size, content_size, chunk_size)
        download_time = round(time.time() - start, 2)
        print(f'共耗时{download_time}秒, 平均速度为:{round(float(content_size / download_time / chunk_size ** 2), 2)}MB/s')
    except Exception as e:
        print(e.args)

    
if __name__ == "__main__":
    get_vedio()