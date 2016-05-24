#coding=utf8
from django.db import models

# Create your models here.
class Choice(models.Model):
        chioce_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
        def __unicode__(self):
                return self.choice_text

class domain(models.Model):
        domain_name = models.CharField(max_length=200)
        domain_pass = models.CharField(max_length=200)
        def __unicode__(self):
                return self.domain_name


class userprofile(models.Model):
        domain_id = models.CharField(max_length=200)
        password = models.CharField(max_length=200)
        name = models.CharField(max_length=200)
        def __unicode__(self):
                return self.domain_id


#class BookManager(models.Manager):
#       def title_count(self,keyword):




class case(models.Model):
        case_apply = models.ForeignKey(userprofile)                 # case申请人，与用户关联
        case_statue = models.CharField(max_length=200)              # case状态
        case_program = models.CharField(max_length=200)             # case归属项目
        case_contact = models.CharField(max_length=200)             # case联系人
        case_summery =models.CharField(max_length=200)              # case摘要（申请人填写）
        case_date = models.DateField(auto_now=True)                 # case日期（生成caseID用）
        case_create_time = models.DateTimeField(auto_now_add=True)  # case创建时间（以主管确认case时间为准）
        case_respond_time = models.DateTimeField(auto_now_add=True) # case响应时间（以工程师相应时间为准）
        case_resolve_time = models.DateTimeField(auto_now_add=True) # case解决时间（以工程师确认解决时间为准）
        case_close_time = models.DateTimeField(auto_now_add=True)   # case关闭时间 （以客服回访时间为准）
        case_respond_overtime = models.BooleanField(default=False)               # case响应超时（是/否）
        case_resolve_overtime = models.BooleanField(default=False)               # case解决超时（是/否）
        case_type = models.CharField(max_length=200)                # case类型
        case_category= models.CharField(max_length=200)             # case类别（售前，售后）
        case_level = models.CharField(max_length=200)               # case级别（一二三四级）
        case_resolver = models.CharField(max_length=200)            # case处理人
        case_id = models.IntegerField(default=0)                    # case——id
        case_resolve_method = models.CharField(max_length=200)            # case处理方式（远程/现场）
        case_resolve_process = models.CharField(max_length=200)            # case处理过程（处理人填写）
        def __unicode__(self):
                return self.case_contact


#class time(models.Model):
#       name = models.CharField(max_length=200)
#       case_create_time = models.DateTimeField(auto_now_add=True)
