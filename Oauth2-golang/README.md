# 代码示例

```go
package main

import (
	"fmt"
	"github.com/haozibi/WeiboSpider/Oauth2"
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
