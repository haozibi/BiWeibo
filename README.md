# BiWeibo

*微博 Oauth2 封装*

* **Golang** 版本 => Golang
* **Python3** 版本 => Python3 + requests


## OAuth2.0的封装

[微博授权机制说明](http://open.weibo.com/wiki/%E6%8E%88%E6%9D%83%E6%9C%BA%E5%88%B6%E8%AF%B4%E6%98%8E)

**使用方法**: 注册微博App后，可以获得app key和app secret，然后定义网站回调地址

## Python3 代码示例

```python
from BiOAuth import *

appKey = '你的app key'
appSecret = '你的app secret'
redirectUri = '你的callback url'
cookies = '用户的cookie'

a = BiOAuth(appKey = appKey,appSecret = appSecret,redirectUri = redirectUri,cookies = cookies)
access_token = a.getAccessToken()
```

## Golang 代码示例

> go get github.com/haozibi/BiWeibo

```go
package main

import (
	"fmt"
	Oauth2 "github.com/haozibi/BiWeibo/Oauth2-golang"
)

func main() {
	a := Oauth2.Oauth{
		AppKey:      "你的AppKey",
		AppScret:    "你的AppScret",
		RedirectUrl: "回调地址",
		Cookie:      "你的Cookie",
	}
	fmt.Println(a.GetToken())
}

```
*由于一般是我个人使用，所以使用cookie判断登录*

*当拥有的access_token后就可以调用其他API，注意acces_token时效性即可*

