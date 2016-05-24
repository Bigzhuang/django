import urllib


def get_menu(token):
    url_get_menu='https://api.weixin.qq.com/cgi-bin/menu/get?access_token='+token
    print url_get_menu
    page=urllib.urlopen(url_get_menu)
    menu=page.read()
    print menu
def delete_menu(token):
    url_del_menu="https://api.weixin.qq.com/cgi-bin/menu/delete?access_token="+token
    response=urllib.urlopen(url_del_menu).read()
    print response
    return None
def get_openid(token):
    url="https://api.weixin.qq.com/cgi-bin/user/get?access_token="+token+"&next_openid="
    print url
    f=urllib.urlopen(url)
    data=f.read()
    return data

def create_menu(token,values):
    try:
        url='https://qyapi.weixin.qq.com/cgi-bin/menu/create?access_token='+token+'&agentid=0'
        print url
        #data=urllib.urlencode(values)
        #print data
        page=urllib.urlopen(url,values)
        print page.read()
    except TypeError,e:
        print  e