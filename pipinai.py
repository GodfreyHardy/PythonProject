# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 21:15:51 2022

@author: littlewood
"""
# pip install requests
import requests
# pip install bs4 用BeautifulSoup来对HTML文档进行解析
from bs4 import BeautifulSoup
import os

urlt = []
class spider():
    def __init__(self, url):
        # 请求网址
        self.url = url
        # 设置请求头
        self.headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36"}

    def get(self):
        # 通过请求获取响应数据（此数据是html文本格式的数据）

        res = requests.get(self.url, headers=self.headers)
        html = res.text

        # 解析数据
        info = BeautifulSoup(html, "lxml")
        # 使用select选择器定位数据
        # data = info.select("body > div:nth - child(9) > div > div > div > div.article - content > img")
        data = info.find('div',class_="article-content")
        # body > div:nth-child(9) > div > div > div > div:nth-child(2) > ul
        # url存入列表中，得到一个urllist列表

        #urllist = data.findAll(name='a')
        # print(len(urllist))
        # for i in range(len(urllist)):
        #     s = str(urllist[i])
        #     if i%2 == 1:
        #         s = s.split('title')
        #         s0 = s[0][9:len(s[0])-2]
        #         s0 = 'https://kanmeitu1.cc'+s0
        #         print("'"+s0+"'"+',')

        imglist = data.findAll(name='img')
        print(imglist)
        urllist = []
        for item in imglist:
            # 在解析后的数据中通过遍历的方法提取图片的u
            picurl = str(item).split('src=')
            #print(picurl[1][1:len(picurl[1])-3])
            urllist.append(picurl[1][1:len(picurl[1])-3])

        #通过解析后的url再次发送请求获取图片
        for j in urllist:
            pictureurl = j
            # 图片命名
            # name = pictureurl.split("/")[-1]
            response = requests.get(url=pictureurl, headers=self.headers)
            # 以二进制数据流的方式写入指定目录文件9
            global number
            with open("D:/spiderPicture/pudding2/%d.jpg" % number, "wb") as f:
                f.write(response.content)
            number += 1


path = "D:/spiderPicture/pudding2"
dirs = os.listdir(path)
number = len(dirs) + 1

# lt = [  'https://kanmeitu1.cc/p/48157.html',
#         'https://kanmeitu1.cc/p/47207.html',
#         'https://kanmeitu1.cc/p/47178.html',
#         'https://kanmeitu1.cc/p/47070.html',
#         'https://kanmeitu1.cc/p/47004.html',
#         'https://kanmeitu1.cc/p/46957.html',
#         'https://kanmeitu1.cc/p/46923.html',
#         'https://kanmeitu1.cc/p/46209.html',
#         'https://kanmeitu1.cc/p/44249.html',
#         'https://kanmeitu1.cc/p/41793.html',
#         'https://kanmeitu1.cc/p/41667.html',
#         'https://kanmeitu1.cc/p/41650.html',
#         'https://kanmeitu1.cc/p/41585.html',
#         'https://kanmeitu1.cc/p/41517.html',
#         'https://kanmeitu1.cc/p/41504.html',
#         'https://kanmeitu1.cc/p/41500.html',
#         'https://kanmeitu1.cc/p/41499.html',
#         'https://kanmeitu1.cc/p/41498.html',
#         'https://kanmeitu1.cc/p/41493.html',
#         'https://kanmeitu1.cc/p/41485.html',
#         'https://kanmeitu1.cc/p/41463.html',
#         'https://kanmeitu1.cc/p/41459.html',
#         'https://kanmeitu1.cc/p/41450.html',
#         'https://kanmeitu1.cc/p/39832.html',
#         'https://kanmeitu1.cc/p/39828.html',
lt  = [
        'https://kanmeitu1.cc/p/37697.html',
        'https://kanmeitu1.cc/p/34993.html',
        'https://kanmeitu1.cc/p/34988.html']

for i in range(0, len(lt)):
    url = lt[i]
    print(url)
    sp = spider(url)
    sp.get()

