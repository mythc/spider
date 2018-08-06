# _*_ coding: utf-8 _*_
import requests
import sys
from bs4 import BeautifulSoup

"""
类说明：下载笔趣阁网站小说：url:http://www.biquge.com.tw/

parameters:
    target - 笔趣阁网站指定小说的目录地址(string)
    
returns:
    null
    
modify:
    2018-08-1
"""
class downloader(object):

    def __init__(self):
        self.server = 'http://www.biquge.com.tw'
        self.target = 'http://www.biquge.com.tw/18_18820'
        self.names = []
        self.urls = []
        self.nums = 0

    def get_download_url(self):
        req = requests.get(url=self.target)
        req.encoding = 'gbk'
        html = req.text
        div_bf = BeautifulSoup(html, 'html.parser')
        div = div_bf.find_all('div', id = 'list')
        a_bf = BeautifulSoup(str(div[0]), 'html.parser')
        a = a_bf.find_all('a')
        self.nums = len(a)
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url = target)
        req.encoding = 'gbk'
        html = req.text
        bf = BeautifulSoup(html, 'html.parser')
        texts = bf.find_all('div', id = 'content')
        texts = texts[0].text.replace('\xa0'*4, '')
        return texts

    def writer(self, name, path, text):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:
            f.write(name + '\n')
            f.writelines(text)
            f.write('\n\n')

    # def down(self, name, path, html):


if __name__ == '__main__':
    dl = downloader()
    dl.get_download_url()
    print('开始下载《飞剑问道》：')
    for i in range(dl.nums):
        dl.writer(dl.names[i], '飞剑问道.txt', dl.get_contents(dl.urls[i]))
        sys.stdout.write('  已下载：%.2f%%' % float(i/dl.nums * 100) + '\r')
        sys.stdout.flush()
        # print("+++")

    print('《飞剑问道》下载完成')



    # server = 'http://www.biquge.com.tw'
    # target = 'http://www.biquge.com.tw/18_18820/'
    # req = requests.get(url=target)
    # req.encoding = 'gbk'
    # html = req.text
    # div_bf = BeautifulSoup(html, 'html.parser')
    # div = div_bf.find_all('div', id = 'list')
    # a_bf = BeautifulSoup(str(div[0]), 'html.parser')
    # a = a_bf.find_all('a')
    # print(a)
    # for each in a:
    #     print(each.string, server + each.get('href'))

    # bf = BeautifulSoup(html,'html.parser')
    # # print(bf)
    # texts = bf.find_all('div', id='content')
    # print(texts[0].text.replace('\xa0'*4, ''))
