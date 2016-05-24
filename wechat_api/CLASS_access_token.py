import urllib
class access_token(object):
    APPID='wx31b6a79b6dbc8449'
    APPSECRET='499df76b2107c129ad4fbe73c47ad354'
    def get_token(slef):
        page=urllib.urlopen('https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&'+'appid='+self.APPID+'&'+'secret='+self.APPSECRET)
        token=self.page.read()
        token=token.split('"')
        return token[3]