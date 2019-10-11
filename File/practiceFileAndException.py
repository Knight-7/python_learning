"练习对文件的操作和异常"
import math
import json


def main():
    try:
        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            for line in f:
                print(line)

        with open('致橡树.txt', 'r', encoding='utf-8') as f:
            lines = f.readlines()
        print('\n', lines)

    except FileNotFoundError:
        print('未找到文件')

    except LookupError:
        print('指点了未知的编码')

    except UnicodeDecodeError:
        print('读取文件时解码错误')


def is_prime(n):
    """使用ACM的方法"""
    assert n > 0
    if n == 2 or n == 3:
        return True
    elif n % 6 != 1 and n % 6 != 5:
        return False
    else:
        for factor in range(5, int(math.sqrt(n)) + 1):
            if n % factor == 0:
                return False
    return True if n != 1 else False


def save_prime():
    """保存1到1000以内的质数"""
    file_names = ('质数.txt', '非质数.txt')
    file_list = []
    try:
        for file_name in file_names:
            file_list.append(open(file_name, 'w', encoding='utf-8'))
        for number in range(2, 1001):
            if is_prime(number):
                file_list[0].write(str(number) + ' ')
            else:
                file_list[1].write(str(number) + ' ')
    except IOError as e:
        print(e)
        print("读写文件时发生错误")
    finally:
        for file in file_list:
            file.close()
    print('保存完成')


def saveasjson():
    mydic = {
        'name':'Knight',
        'age':22,
        'qq':1252809618,
        'friend':['1', '2', '3'],
        'courses':[
            {'name':'计算机网络技术', 'time':'48课时'},
            {'name':'数据库基础', 'time':'32课时'},
            {'name':'计算机操作系统', 'time':'48课时'}
        ]
    }
    try:
        with open('data.json', 'w', encoding='utf-8') as f:
            json.dump(mydic, f) # 将python对象按照json格式序列到文件中
    except IOError as e:
        print(e)


def readfromjson():
    try:
        with open('date.json', 'r', encoding='utf-8') as f:
            mydic = json.load(f)
            return mydic
    except FileNotFoundError:
        print('没有找到文件')


if __name__ == '__main__':
    # main()
    # save_prime()
    # saveasjson()
    mydic = readfromjson()
    try:
        for k, v in mydic.items():
            print(k, v, sep=':')
    except AttributeError as e:
        print(e)