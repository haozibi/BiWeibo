package Oauth2

const (
	AuthorizeUrl   = "https://api.weibo.com/oauth2/authorize"
	AccessTokenUrl = "https://api.weibo.com/oauth2/access_token"
)

type OauthJson struct {
	Access_token string `json:"access_token"`
	Remind_in    string `json:"remind_in"`
	Expires_in   int    `json:"expires_in"`
	Uid          string `json:"uid"`
}
