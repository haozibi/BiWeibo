#!/usr/bin/env python3
# coding = utf-8

from BiOAuth import *

appKey = '你的app key'
appSecret = '你的app secret'
redirectUri = '你的callback url'
cookies = '用户的cookie'

a = BiOAuth(appKey = appKey,appSecret = appSecret,redirectUri = redirectUri,cookies = cookies)
b = a.getAccessToken()
print('access_token' + b)