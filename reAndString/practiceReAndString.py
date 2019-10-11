# 练习正则表达式和字符串
import re #今天可了一半的正则表达式，明天再看另一半


def main():
    pass


def check_account_and_name():
    """
    验证输入用户名和qq号是否有效并给出对应的提示

    要求：用户名必须由字母、数字或下划线构成且长度在6-20之间
    QQ号是5-12的数字且首位不为0
    """
    userName = input('请输入用户名: ')
    qq = input('请输入QQ号： ')

    # 在字符串前面加上r表示使用了原始字符串，即字符串中的每个字符都是它的原始的意义，说的更直接一点就是字符串中没有所谓
    # 为的转义字符
    m1 = re.match(r'^[0-9a-zA-Z_]{6,20}$', userName)
    if not m1:
        print('请输入正确的用户名')
    m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    if not m2:
        print('请输入有效的qq号')
    if m1 and m2:
        print('你输入的信息是有效的')


def check_number():
    """
    从一段文字中提取国内的手机号码
    """
    sentence = """
    重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
    不是15600998765，也是110或119，王大锤的手机号才是15600998765。
    """
    pattern = re.compile(r'(?<=\D)(1[38]\d{9}|14[57]\d{8}|15[0-35-9]\d{8}|17[678]\d{8})(?=\D)')
    # 将查找中所有匹配的保存到一个列表中
    mylist = re.findall(pattern, sentence)
    print(mylist)
    # 通过迭代器取出匹配对象并获得匹配的内容
    print('----------华丽的分割线-----------')
    for temp in pattern.finditer(sentence):
        print(temp.group())
    print('-----------华丽的分割线----------')
    # 通过search函数指定搜索位置找出所有匹配
    m = pattern.search(sentence)
    while m:
        print(m.group())
        m = pattern.search(sentence, m.end())


def change_something():
    sentence = '你丫是傻叉吗? 我操你大爷的. Fuck you.'
    purified = re.sub('[操肏艹草曹]|fuck|shit|傻[比屄逼叉缺吊屌]|煞笔',
                      '*', sentence, flags=re.IGNORECASE)
    print(purified)


def split_poem():
    poem = '窗前明月光，疑是地上霜。举头望明月，低头思故乡。'
    sentence_list = re.split(r'[，。,.]', poem)
    while ' ' in sentence_list:
        sentence_list.remove(' ')
    print(sentence_list)


if __name__ == '__main__':
    main()
    # check_account_and_name()
    check_number()
    change_something()
    split_poem()