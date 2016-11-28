#!/usr/bin/env python3
# coding = utf-8

__version__ = '0.1.1'
__author__  = 'haozibi (b@ydo.io)'

# auther : haozibi
# web : http://ydo.io

import requests, json, time

class BiOAuth:
    #设定一些初始值
    def __init__(self,appKey,appSecret,redirectUri,cookies):
        self.appKey = appKey
        self.appSecret = appSecret
        self.redirectUri = redirectUri
        self.oauth2Authorize = 'https://api.weibo.com/oauth2/authorize'
        self.oauth2Token = 'https://api.weibo.com/oauth2/access_token'
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.87 Safari/537.36',
                        'Referer':'http://weibo.com/bpython/home'
                        }
        self.cookies = dict(cookies_are=cookies)


    #设置某些属性
    def setAppKey(self,appKey):
        self.appKey = appKey
    def setAppsecret(self,appSecret):
        self.appSecret = appSecret
    def setCookies(self,cookie):
        self.cookies = dict(cookies_are=cookies)
    def setRedirectUri(self,url):
        self.redirectUri = url

    #查看设置属性的值
    def getAppKey(self):
        return self.appKey
    def getAppsecret(self):
        return self.appSecret
    def getCookies(self):
        return self.cookie
    def getRedirectUri(self):
        return self.redirectUri


    #登录授权第一步，
    #生成code指定链接
    def getAPIUrl(self):
        data_oauth2 = {
            'client_id':self.appKey,
            'redirect_uri':self.redirectUri
        }

        tmp_url = requests.get(self.oauth2Authorize,params=data_oauth2)
        ##print('授权连接：' + tmp_url.url)
        return tmp_url.url


    #登录授权第一步，
    #获取code值
    def getAPICode(self,one_url):
        s = requests.Session()
        a = s.get(one_url,headers=self.headers,cookies=self.cookies)
        ##print('重定向链接：' + a.url)
        tmp_num = a.url.find('?')
        if a.url[0:tmp_num] == self.redirectUri:
            code = a.url[tmp_num+6:]
            return code

    #登录授权第二步，获取access_token
    def getAccessTokenTwo(self,code):
        data_oauth2_token = {
            'client_id':self.appKey,
            'client_secret':self.appSecret,
            'grant_type':'authorization_code',
            'code':code,
            'redirect_uri':self.redirectUri,
        }

        tmp_url = requests.post(self.oauth2Token,data=data_oauth2_token)
        tmp_thing = json.loads(tmp_url.text)
        access_token = tmp_thing['access_token'] #有效期为一天
        #print('access_token：' + access_token)
        return access_token


    def getAccessToken(self):
        tmp_a = self.getAPIUrl()
        tmp_a = self.getAPICode(tmp_a)
        ##print(tmp_a)
        return self.getAccessTokenTwo(tmp_a)