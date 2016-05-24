import urllib
class get_token(object):

    def __init__(self,appid,appsecret):
        self.appid=appid
        self.appsecret=appsecret
    def get_access_token(self):
        resp=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+self.appid+'&corpsecret='+self.appsecret).read()
#        token=resp.read()
        resp=resp.split('"')
        resp=str(resp[3])
        return resp


#def get_token(appid,appsecret):
#        resp=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+appid+'&corpsecret='+appsecret).read()
#       print resp
#       return resp


appid='wx7f45564ffab82f2d';appsecret='CLvAoK78XZuqtT9z-lOQ9LE28Yfgpjymoyly1UtBtgZSKZhAO_yhEwQ9-EbaboH_'
#resp=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid='+appid+'&corpsecret='+appsecret).read()
#print resp
wx=get_token(appid,appsecret)
token=wx.get_access_token()
print token

with open('/root/mysite/token.txt','wa')as f:
       f.write(token)
