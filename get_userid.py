#encoding=utf8
import urllib,json
from django.http import HttpResponseRedirect
def get_user_profile(ACCESS_TOKEN,USERID):                      #通过userid获得用户信息
        page=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token='+ACCESS_TOKEN+'&userid='+USERID).read()
        return page


#with open('/root/mysite/token.txt','r')as f:
#       token=f.read()
#print 'token='+token
#user=get_user_profile(token,'xuyizhou')
#print user

def find_director(ACCESS_TOKEN,DEPARTMENT_ID):                  #通过部门ID分析成员信息找出主管的userid
        page=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/user/list?access_token='+ACCESS_TOKEN+'&department_id='+DEPARTMENT_ID+'&fetch_child=1&status=0')
        department_partner=page.read()
        user_list=json.loads(department_partner)
        for i in user_list['userlist']:
                if 'position' in i:
                        if i['position']=='director':
                                user_id=i['userid']
                                return user_id

def if_login(func):
        def wrapper(req):
                if not req.COOKIES.get('userid',''):
                        HttpResponseRedirect('/case/')
                        print 'hehe'
                return func(req)
        return wrapper



def sent_case_director(ACCESS_TOKEN,director,userid,chinese_name,case_id):                   #通过主管的userid将case提交给主管
        data='''{
   "touser":'''+'"'+str(director)+'"'+''',
   "msgtype": "text",
   "agentid": "0",
   "text": {
       "content": "你有一个来自'''+chinese_name+'''的case需要处理(http://weixin.rayking.com.cn/case_verify/?id='''+case_id+''')"
   },
   "safe":"0"
}'''
        page=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+ACCESS_TOKEN,data)
        response=page.read()
        return response


def sent_case_assigner(ACCESS_TOKEN,userid,case_id):                   #通过userid将case发给case创建人
        data='''{
   "touser":'''+'"'+str(userid)+'"'+''',
   "msgtype": "text",
   "agentid": "0",
   "text": {
       "content": "你申请的case（id='''+case_id+'''）已被主管确认,请尽快响应(http://weixin.rayking.com.cn/case_response/?id='''+case_id+''')"
   },
   "safe":"0"
}'''
        page=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token='+ACCESS_TOKEN,data)
        response=page.read()
        return response






if __name__=='__main__':
        with open('/root/mysite/token.txt','r')as f:
                ACCESS_TOKEN=f.read()
        userid='xuyizhou'
        message=get_user_profile(ACCESS_TOKEN,userid)
        message=str(json.loads(message)['department'])
        print message[1]


































#def get_userid(CODE,ACCESS_TOKEN,agentid): #未知功能
#    page=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/user/getuserinfo?access_token='+ACCESS_TOKEN+'&code='+CODE+'&agentid='+agentid)
#    userid=page.read()
#    return userid

#def auth_success(ACCESS_TOKEN,USERID):
#       page=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/user/authsucc?access_token='+ACCESS_TOKEN+'&userid='+USERID)
#       success_code=page.read()
#       return  success_code
