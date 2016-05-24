import urllib

def get_userid(CODE,ACCESS_TOKEN,agentid):
    page=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+ACCESS_TOKEN+'&code='+CODE+'&agentid='+agentid)
    userid=page.read()
    print userid
    
get_userid(code,ACCESS_TOKEN,agentid)