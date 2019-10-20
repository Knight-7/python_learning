from urllib.parse import urljoin

import re
import requests

from bs4 import BeautifulSoup


def get_movie_name(html):
    regex = r'alt="(w+)"|《(w+)》|'
    pass


def get_link():
    headers = {'user-agent': 'Baiduspider'}
    proxies = {
        'http': 'http://122.114.31.177:808'
    }
    base_url = 'https://movie.douban.com/'
    resp = requests.get(base_url,
                        headers=headers,
                        proxies=proxies)
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^https://movie.douban.com/subject')
    link_inf = set()
    soup_res = soup.find_all('a', {'href': href_regex})
    for a_tag in soup_res:
        print(a_tag.prettify())
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_link = urljoin(base_url, href)
            link_inf.add(full_link)
    print(f'一共获得了{len(link_inf)}个链接')
    for link in link_inf:
        print(link)


def get_name():
    headers = {'user-agent': 'Baiduspider'}
    proxies = {
        'http': 'http://122.114.31.177:808'
    }
    base_url = 'https://movie.douban.com/'
    resp = requests.get(base_url,
                        headers=headers,
                        proxies=proxies)
    soup = BeautifulSoup(resp.text, 'lxml')
    href_regex = re.compile(r'^https://movie.douban.com/subject')
    link_inf = set()
    print(soup.find_all())
    soup_res = soup.find_all('a')
    print(soup_res)
    for a_tag in soup_res:
        # print(a_tag)
        if 'href' in a_tag.attrs:
            href = a_tag.attrs['href']
            full_link = urljoin(base_url, href)
            link_inf.add(full_link)
    for link in link_inf:
        print(link)


if __name__ == '__main__':
    get_link()
    # get_name()