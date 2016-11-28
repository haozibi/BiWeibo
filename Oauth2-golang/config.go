package Oauth2

import (
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"strings"
)

type Oauth struct {
	AppKey      string
	AppScret    string
	RedirectUrl string
	Cookie      string
}

func (o *Oauth) GetAppKey() (appKey string, err error) {
	if o.AppKey == "" {
		return
	}
	return o.AppKey, nil
}

func (o *Oauth) GetRedirectUrl() (uri string) {
	return o.RedirectUrl
}

func (o *Oauth) RemoveAll() {
	o.AppKey = ""
	o.AppScret = ""
	o.Cookie = ""
	o.RedirectUrl = ""
}

func (o *Oauth) getAuthorize() (code string) {
	uri := o.getApiUrl()
	req, _ := http.NewRequest("GET", uri, nil)
	req.Header.Add("cache-control", "no-cache")
	if o.Cookie == "" {
		fmt.Println("Cookie is nil")
	} else {
		req.Header.Add("Cookie", o.Cookie)
	}
	res, _ := http.DefaultClient.Do(req)
	defer res.Body.Close()
	code = res.Request.URL.Query()["code"][0]
	fmt.Println("Code:", code)
	return
}

func (o *Oauth) getApiUrl() (uri string) {
	uri = AuthorizeUrl +
		"?client_id=" + o.AppKey +
		"&redirect_uri=" + o.RedirectUrl
	return
}

func (o *Oauth) getAccessToken(code string) (Token string) {
	payload := strings.NewReader(
		"client_id=" + o.AppKey +
			"&client_secret=" + o.AppScret +
			"&grant_type=authorization_code" +
			"&code=" + code +
			"&redirect_uri=" + o.RedirectUrl)
	req, _ := http.NewRequest("POST", AccessTokenUrl, payload)
	req.Header.Add("content-type", "application/x-www-form-urlencoded")
	req.Header.Add("cache-control", "no-cache")

	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	// fmt.Println(string(body))
	var s OauthJson
	json.Unmarshal([]byte(string(body)), &s)
	return s.Access_token
}

func (o *Oauth) GetToken() (code string) {
	code = o.getAuthorize()
	return o.getAccessToken(code)
}
