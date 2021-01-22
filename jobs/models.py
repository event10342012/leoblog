from datetime import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy

# Create your models here.

DEGREE_TYPE = ((u'大學', u'大學'), (u'碩士', u'碩士'), (u'博士', u'博士'))

job_types = [
    (0, 'tech'),
    (1, 'product'),
    (2, 'operation'),
    (3, 'design')
]

cites = [
    (0, 'Taipei'),
    (1, 'Taichung'),
    (2, 'Kaohsiung')
]


class Job(models.Model):
    job_type = models.SmallIntegerField(blank=False, choices=job_types, verbose_name='job_type')
    job_name = models.CharField(max_length=250, blank=False, verbose_name='job_name')
    job_city = models.SmallIntegerField(blank=False, choices=cites, verbose_name='job_city')
    job_responsibility = models.TextField(max_length=1024, verbose_name='job_responsibility')
    job_requirement = models.TextField(max_length=1024, blank=False, verbose_name='job_requirement')
    creator = models.ForeignKey(User, verbose_name='creator', null=True, on_delete=models.SET_NULL)
    created_date = models.DateTimeField(verbose_name='created_date', default=datetime.now)
    modified_date = models.DateTimeField(verbose_name='modify_date', default=datetime.now)


class Resume(models.Model):
    # Translators: 简历实体的翻译
    username = models.CharField(max_length=135, verbose_name=gettext_lazy('姓名'))
    applicant = models.ForeignKey(User, verbose_name=gettext_lazy("申请人"), null=True, on_delete=models.SET_NULL)
    city = models.CharField(max_length=135, verbose_name=gettext_lazy('城市'))
    phone = models.CharField(max_length=135, verbose_name=gettext_lazy('手機號碼'))
    email = models.EmailField(max_length=135, blank=True, verbose_name=gettext_lazy('郵箱'))
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=gettext_lazy('應徵職位'))
    born_address = models.CharField(max_length=135, blank=True, verbose_name=gettext_lazy('出生地'))
    gender = models.CharField(max_length=135, blank=True, verbose_name=gettext_lazy('性别'))
    picture = models.ImageField(upload_to='images/', blank=True, verbose_name=gettext_lazy('個人照片'))
    attachment = models.FileField(upload_to='file/', blank=True, verbose_name=gettext_lazy('簡歷附件'))

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=gettext_lazy('本科學校'))
    master_school = models.CharField(max_length=135, blank=True, verbose_name=gettext_lazy('研究生學校'))
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'博士生學校')
    major = models.CharField(max_length=135, blank=True, verbose_name=gettext_lazy('專業'))
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=gettext_lazy('學歷'))
    created_date = models.DateTimeField(verbose_name="創建日期", default=datetime.now)
    modified_date = models.DateTimeField(verbose_name="修改日期", auto_now=True)

    # 候选人自我介绍，工作经历，项目经历
    candidate_introduction = models.TextField(max_length=1024, blank=True, verbose_name=u'自我介绍')
    work_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'工作經歷')
    project_experience = models.TextField(max_length=1024, blank=True, verbose_name=u'项目經歷')

    class Meta:
        verbose_name = gettext_lazy('簡歷')
        verbose_name_plural = gettext_lazy('簡歷列表')

    def __str__(self):
        return self.username
