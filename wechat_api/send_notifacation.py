#coding='utf-8'
import urllib
value=''' {
   "touser": "tianlei",
   "toparty": "",
   "totag": "",
   "msgtype": "text",
   "agentid": "0",
   "text": {
       "content": "田老师，几号回呦~"
   },
   "safe":"0"
}'''
f=urllib.urlopen('https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=fM5EPXkc6dM7oeeZcmgOB5TEcQuvUzlFpeZqgJFerc2bum1mvj6gEBNrQFyjemcVTpiqz00Kft_J3WWfNCxhMg',value)

print f.read()