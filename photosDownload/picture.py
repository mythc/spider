# _*_ coding: UTF-8 _*_
import json
import time
from contextlib import closing

import re
import requests


class GetPhotos(object):

    def __init__(self):
        self.photos_id = []
        self.download_server = 'https://unsplash.com/photos/xxx/download?force=trues'
        self.target = 'https://unsplash.com/napi/feeds/home'
        self.headers = {}

    '''
    函数说明： 获取图片id
    Parameters:     无
    Returns:        无
    Modify:         2018-08-02
    '''
    def get_ids(self):
        req = requests.get(self.target)
        print(req.text)
        # for i in range(5):
        html = json.loads(req.text)
        print(html)
        next_page = html['next_page']
        for each in html['photos']:
            self.photos_id.append(each['id'])
        # req = requests.get(next_page)
        # print(req.text)
        time.sleep(1)
        for i in range(10):
            api = re.search(r'after=(.*)', next_page).group(1)
            print(api)
            next_page = 'https://unsplash.com/napi/feeds/home?after='+api
            req = requests.get(next_page)
            html = json.loads(req.text)
            next_page = html['next_page']
            for each in html['photos']:
                self.photos_id.append(each['id'])
            time.sleep(1)

    '''
    函数说明：       图片下载
    Parameters:     无
    Returns:        无
    Modify:         2018-08--03'''
    def download(self, photo_id, filename):
        target = self.download_server.replace('xxx', photo_id)
        with closing(requests.get(target)) as r:
            with open('%d.jpg' % filename, 'ab+') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        f.write(chunk)
                        f.flush()


if __name__ == '__main__':
    gp = GetPhotos()
    print('获取图片连接中：')
    gp.get_ids()
    print('图片下载中：')
    for i in range(len(gp.photos_id)):
        print('  正在下载第%d张图片' % (i+1))
        gp.download(gp.photos_id[i], (i+1))

