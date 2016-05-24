import urllib
class get_token(object):
    
    def __init__(self,appid,appsecret):
        self.appid=appid
        self.appsecret=appsecret
    def get_access_token(self):
        resp=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+self.appid+'&corpsecret='+self.appsecret)
        token=resp.read()
        token=token.split('"')
        token=str(token[3])
        print token
        return token

#APPID='wx7f45564ffab82f2d'
#APPSECRET='CLvAoK78XZuqtT9z-lOQ9LE28Yfgpjymoyly1UtBtgZSKZhAO_yhEwQ9-EbaboH_'        
#wx=get_token(APPID,APPSECRET)
#wx.get_access_token()