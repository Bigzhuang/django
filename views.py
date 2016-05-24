#!/usr/bin/env python
# encoding: utf-8
# 访问 http://tool.lu/pyc/ 查看更多信息
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from module.get_userid import *
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.encoding import smart_str
from django.views.decorators.csrf import csrf_exempt
from lxml import etree
from weixin.models import userprofile
from weixin.models import case
import ldap
import datetime
import base64
from django.http import HttpResponseRedirect
import time

@csrf_exempt
def home_page(request):
    if 'favorite_color' in request.COOKIES:
        return HttpResponse('hehe you have cookie')
    response = None('hehe')
    response.set_cookie('favorite_color', 'red', 3600)
    return response

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
@csrf_exempt
def IdBind(request):
    if request.method == 'GET':
        return render(request, 'idbind.html')

##########################################################################################################################

def IdBind_process(request):
    if request.method == 'POST':
        error = []
        if not request.POST['name']:
            error.append('hehe')
            return HttpResponse('input name')
        if not request.POST['password']:
            error.append('hehe')
            return HttpResponse('input password')
        if error == []:
            ldap_user = request.POST.get('domain_id', None)
            password = request.POST.get('password', None)
            name = request.POST.get('name', None)
            con = ldap.initialize('ldap://10.10.1.24')
            ldap_pass = password

            try:
                respon = con.simple_bind_s(ldap_user, ldap_pass)
            except ldap.LDAPError:
                e = None
                error_message = '\xe9\x94\x99\xe8\xaf\xaf\xe7\x9a\x84\xe7\x94\xa8\xe6\x88\xb7\xe5\x90\x8d\xe6\x88\x96\xe5\xaf\x86\xe7\xa0\x81\xef\xbc\x81'
                context = {
                    'error': error_message }
                return render(request, 'idbind.html', context)

            con.unbind()
            if not userprofile.objects.filter(domain_id = ldap_user.split('@')[0]):
                ldap_pass = base64.b64encode(ldap_pass)
                userprofile.objects.create(name = name, password = ldap_pass, domain_id = ldap_user.split('@')[0])
                bind_success = '\xe6\x81\xad\xe5\x96\x9c\xe4\xbd\xa0\xef\xbc\x8c\xe7\xbb\x91\xe5\xae\x9a\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x81\xef\xbc\x81\xef\xbc\x81'
                context = {
                    'bind_success': bind_success,
                    'username': ldap_user }
                response = render(request, 'idbind.html', context)
                response.set_cookie('chinesename', name, 10368000)
                response.set_cookie('userid', ldap_user.split('@')[0], 10368000)
                return response
            if None not in request.COOKIES:
                rebinded = '\xe9\x87\x8d\xe7\xbb\x91\xe5\xae\x9a\xe6\x88\x90\xe5\x8a\x9f\xef\xbc\x81\xef\xbc\x81\xef\xbc\x81'
                context = {
                    'binded': rebinded }
                response = HttpResponseRedirect('/case/')
                response.set_cookie('chinesename', name, 10368000)
                response.set_cookie('userid', ldap_user.split('@')[0], 10368000)
                return response
            if None in request.COOKIES:
                binded = '\xe6\x82\xa8\xe5\xb7\xb2\xe7\xbb\x91\xe5\xae\x9a\xe8\xbf\x87\xef\xbc\x8c\xe8\xaf\xb7\xe5\x8b\xbf\xe9\x87\x8d\xe5\xa4\x8d\xe7\xbb\x91\xe5\xae\x9a'
                context = {
                    'binded': binded }
                response = render(request, 'idbind.html', context)
                return response

IdBind_process = csrf_exempt(IdBind_process)

##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
def case_request(request):
    values = request.META.items()
    html = []
    for (k, v) in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))

    print 'html:   ', html
    return HttpResponse('<table>%s</table>' % '\n'.join(html))

case_request = csrf_exempt(case_request)

##########################################################################################################################
def case_new(request):
    if 'chinesename' in request.COOKIES:
        username = request.COOKIES.get('chinesename', '')
        context = {
            'username': username }
        return render(request, 'case.html', context)
    change_message = None
    context = {
        'change_message': change_message }
    return render(request, 'idbind.html', context)

case_new = csrf_exempt(case_new)

##########################################################################################################################
def case_preview(request):
    if request.method == 'POST':
        case_detail = request.POST.items()
        user_name = case_detail[0][1]
        case_reason = case_detail[1][1]
        program_name = case_detail[2][1]
        time_now = time.strftime('%Y-%m-%d %X %p', time.localtime())
        user_id = request.COOKIES.get('userid', '')
        today = datetime.date.today()
        before = case.objects.filter(case_date=datetime.date.today())
        case_id = today.year*(10**6)+today.month*(10**4)+today.day*100+before.count()+1
        user_object = userprofile.objects.get(domain_id = user_id)
        case_object = case.objects.create(case_statue = '\xe5\xbe\x85\xe7\xa1\xae\xe8\xae\xa4', case_program = program_name, case_contact = user_name, case_summery = case_reason, case_apply_id = user_object.id ,case_id=case_id)
        context = {
            'name': program_name,
            'customer': user_name,
            'time': time_now,
            'reason': case_reason }
        response = render(request, 'preview.html', context)
        response.set_cookie('case_id', case_object.id, 10368000)
        return response

case_preview = csrf_exempt(case_preview)

##########################################################################################################################
@csrf_exempt
def case_submit(request):
    with open('/root/mysite/token.txt', 'r') as f:
        ACCESS_TOKEN = f.read()
    user_id = request.COOKIES.get('userid', '')
    print 'user_id is' + user_id
    case_id = request.COOKIES.get('case_id', '')
    chinese_name = request.COOKIES.get('chinesename', '')
    print 'case_id is' + case_id
    department = get_user_profile(ACCESS_TOKEN, user_id)
    department = str(json.loads(department)['department'])
    director_id = find_director(ACCESS_TOKEN, department[1])
    response = sent_case_director(ACCESS_TOKEN, director_id, user_id, chinese_name, case_id)
    context = {
        'director': director_id }
    return render(request, 'case_send_success.html', context)

##########################################################################################################################


def case_verify(request):
    case_id = request.GET['id']
    c = case.objects.get(id = case_id)
    if c.case_statue!='待确认':
        return HttpResponse('你已确认过该CASE，请等待工程师相应')
    else:
#        (case_statue, case_program, case_contact, case_create_time, case_summery) = (c.case_statue, c.case_program, c.case_contact, c.case_create_time, c.case_summery)
        context = {
            'company': c.case_program,
            'contact': c.case_contact,
            'summery': c.case_summery,
            'create_time': c.case_create_time,
            'case_statue': c.case_statue,
            'case_id':c.case_id }
        respon = render(request, 'verify.html', context)
        respon.set_cookie('case_id', case_id, 10368000)
        return respon

case_verify = csrf_exempt(case_verify)

##########################################################################################################################

def case_assign(request):
    case_type = request.POST['case_type']
    case_level = request.POST['case_level']
    case_category = request.POST['case_category']
    case_id = request.COOKIES.get('case_id', None)
    obj = case.objects.get(id = case_id)
    obj.case_type = case_type
    obj.case_level = case_level
    obj.case_category = case_category
    obj.case_create_time = datetime.datetime.now()
    obj.case_statue = '\xe5\xbe\x85\xe5\x93\x8d\xe5\xba\x94'
    obj.save()
    case_statue = obj.case_statue
    case_program = obj.case_program
    case_contact = obj.case_contact
    case_create_time = obj.case_create_time
    case_summery = obj.case_summery
    case_creater = obj.case_apply.name
    context = {
        'company': case_program,
        'contact': case_contact,
        'summery': case_summery,
        'create_time': case_create_time,
        'case_statue': case_statue,
        'type': case_type,
        'level': case_level,
        'category': case_category }
    respon = render(request, 'assign.html', context)
    respon.set_cookie('case_creater', case_creater, 10368000)
    return respon

case_assign = csrf_exempt(case_assign)

##########################################################################################################################

def case_sendback(request):
    if 'case_creater' in request.COOKIES:
        case_creater = request.COOKIES.get('userid', '')
        case_id = request.COOKIES.get('case_id', '')
        f = open('/root/mysite/token.txt', 'r+')
        token = f.read()
        f.close()
        sent_case_assigner(token, case_creater, case_id)
        return HttpResponse('case已交由')

case_sendback = csrf_exempt(case_sendback)
