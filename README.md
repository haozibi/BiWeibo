# BiWeibo

*Python3微博API封装*

## 环境与依赖

* python3
* requests(pip install requests)

## OAuth的封装

[微博授权机制说明](http://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6%E8%AF%B4%E6%98%8E)

**使用方法**: 注册微博App后，可以获得app key和app secret，然后定义网站回调地址
```
from BiOAuth import *

appKey = '你的app key'
appSecret = '你的app secret'
redirectUri = '你的callback url'
cookies = '用户的cookie'

a = BiOAuth(appKey = appKey,appSecret = appSecret,redirectUri = redirectUri,cookies = cookies)
access_token = a.getAccessToken()
```

*由于一般是我个人使用，所以使用cookie判断登录*

*当拥有的access_token后就可以调用其他API，注意acces_token时效性即可*

