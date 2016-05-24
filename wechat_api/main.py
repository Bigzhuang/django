#encoding=utf8
import urllib
import json
from get_userid import *
from get_token import *
APPID='wx7f45564ffab82f2d'
APPSECRET='CLvAoK78XZuqtT9z-lOQ9LE28Yfgpjymoyly1UtBtgZSKZhAO_yhEwQ9-EbaboH_'
wx=get_token(APPID,APPSECRET)
token=wx.get_access_token()

values='''{
    "button": [
        {
            "name": "员工通道", 
            "sub_button": [
                {
                    "type": "view", 
                    "name": "新建CASE", 
                    "url": "http://weixin.rayking.com.cn/case/"
                }, 
                {
                    "type": "view", 
                    "name": "身份绑定", 
                    "url": "http://weixin.rayking.com.cn/idbind/"
                }
            ]
        }, 
        {
            "name": "发图", 
            "sub_button": [
                {
                    "type": "pic_sysphoto", 
                    "name": "系统拍照发图", 
                    "key": "rselfmenu_1_0", 
                   "sub_button": [ ]
                 }, 
                {
                    "type": "pic_photo_or_album", 
                    "name": "拍照或者相册发图", 
                    "key": "rselfmenu_1_1", 
                    "sub_button": [ ]
                }, 
                {
                    "type": "pic_weixin", 
                    "name": "微信相册发图", 
                    "key": "rselfmenu_1_2", 
                    "sub_button": [ ]
                }
            ]
        }, 
        {
            "name": "发送位置", 
            "type": "location_select", 
            "key": "rselfmenu_2_0"
        }
    ]
}
'''


create_menu(token,values)
#openid= get_openid(token)
#openid=json.loads(openid)
#openid=openid[u'data'][u"openid"]
#for i in openid:
#    print i