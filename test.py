import requests


def main():
    r = requests.get('http://www.jianshu.com')
    exit() if not r.status_code == requests.codes.ok else print('Request Successfully')


if __name__ == '__main__':
    main()