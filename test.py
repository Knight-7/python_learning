import requests
import time
import sys

from threading import Thread


def print_process(p_size, size, content_size, chunk_size):
    block_num = int(int(size / content_size * 100) * 0.8)
    blank_num = 80 - block_num
    persent = round(float((size / content_size) * 100), 2)
    speed = round(float((size - p_size) / chunk_size ** 2), 2)
    process_bar = '█' * block_num + ' ' * blank_num + f' {persent}%, {speed}MB/s' + '\r'
    sys.stdout.write(process_bar)
    sys.stdout.flush()
    if int(persent) == 100:
        sys.stdout.write(process_bar)
        sys.stdout.flush()
        print()


def get_vedio():
    start = time.time()
    url = 'https://ugcws.video.gtimg.com/uwMROfz2r57CIaQXGdGnC2deB3dMjwJ3j2-b08CjaiSNycAH/szg_83055102_50001_7f88ea928ce64e79994af38615b7f9dc.f622.mp4?sdtfrom=v1010&guid=946e6728335a4021060eaf32eee43731&vkey=C39301697097862E4FFED5462A0A25C6177496DCD5E0AE68FD095167451C87D85F28BD8CBA7D97257A04493312D3C0CBC965A16115797180F2D88E40A8CBC7097C21A0C6A55D53C0FCC5CB706E3DB7AFACB8D1ACA221230A2F6F0F6B155E03100DAEB65A6F3837179BE3586320697DADBD6008250B24DF79EB0B68ED85E947B3'
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
        print(f'下载完成，耗时{download_time}秒, 平均速度为:{round(float(content_size / download_time / chunk_size ** 2), 2)}MB/s')
    except Exception as e:
        print(e.args)

    
if __name__ == "__main__":
    get_vedio()
