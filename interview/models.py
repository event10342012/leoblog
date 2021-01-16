from django.contrib.auth.models import User
from django.db import models

from jobs.models import DEGREE_TYPE

# 第一轮面试结果
FIRST_INTERVIEW_RESULT_TYPE = ((u'建議複試', u'建議複試'), (u'待定', u'待定'), (u'放棄', u'放棄'))

# 复试面试建议
INTERVIEW_RESULT_TYPE = ((u'建議錄用', u'建議錄用'), (u'待定', u'待定'), (u'放棄', u'放棄'))

# HR终面结论
HR_SCORE_TYPE = (('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C'))


class Candidate(models.Model):
    # 基础信息
    userid = models.IntegerField(unique=True, blank=True, null=True, verbose_name=u'應徵者ID')
    username = models.CharField(max_length=135, verbose_name=u'姓名')
    city = models.CharField(max_length=135, verbose_name=u'城市')
    phone = models.CharField(max_length=135, verbose_name=u'手機號碼')
    email = models.EmailField(max_length=135, blank=True, verbose_name=u'郵箱')
    apply_position = models.CharField(max_length=135, blank=True, verbose_name=u'應徵職位')
    born_address = models.CharField(max_length=135, blank=True, verbose_name=u'出生地')
    gender = models.CharField(max_length=135, blank=True, verbose_name=u'性別')
    candidate_remark = models.CharField(max_length=135, blank=True, verbose_name=u'應徵者訊息備註')

    # 学校与学历信息
    bachelor_school = models.CharField(max_length=135, blank=True, verbose_name=u'大學學校')
    master_school = models.CharField(max_length=135, blank=True, verbose_name=u'研究所學校')
    doctor_school = models.CharField(max_length=135, blank=True, verbose_name=u'博士學校')
    major = models.CharField(max_length=135, blank=True, verbose_name=u'專業')
    degree = models.CharField(max_length=135, choices=DEGREE_TYPE, blank=True, verbose_name=u'學歷')

    # 综合能力测评成绩，笔试测评成绩
    test_score_of_general_ability = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True,
                                                        verbose_name=u'綜合能力評測成績')
    paper_score = models.DecimalField(decimal_places=1, null=True, max_digits=3, blank=True, verbose_name=u'筆試成績')

    # 第一轮面试记录
    first_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'初试分',
                                      help_text=u'1-5分，極優秀: >=4.5，優秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，較差: <3分')
    first_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                 verbose_name=u'學習能力得分')
    first_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                        verbose_name=u'專業能力得分')
    first_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'優勢')
    first_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顧慮與不足')
    first_result = models.CharField(max_length=256, choices=FIRST_INTERVIEW_RESULT_TYPE, blank=True,
                                    verbose_name=u'初試結果')
    first_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'推薦部門')
    first_interviewer_user = models.ForeignKey(User, related_name='first_interviewer_user', blank=True, null=True,
                                               on_delete=models.CASCADE, verbose_name=u'面試官')

    first_remark = models.CharField(max_length=135, blank=True, verbose_name=u'初試備註')

    # 第二轮面试记录
    second_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True, verbose_name=u'專業複試得分',
                                       help_text=u'1-5分，極優秀: >=4.5，優秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，較差: <3分')
    second_learning_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                  verbose_name=u'學習能力得分')
    second_professional_competency = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                         verbose_name=u'專業能力得分')
    second_pursue_of_excellence = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                      verbose_name=u'追求卓越得分')
    second_communication_ability = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                       verbose_name=u'溝通能力得分')
    second_pressure_score = models.DecimalField(decimal_places=1, null=True, max_digits=2, blank=True,
                                                verbose_name=u'抗壓能力得分')
    second_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'優勢')
    second_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顧慮與不足')
    second_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'專業複試結果')
    second_recommend_position = models.CharField(max_length=256, blank=True, verbose_name=u'建議方向或推薦部門')
    second_interviewer_user = models.ForeignKey(User, related_name='second_interviewer_user', blank=True, null=True,
                                                on_delete=models.CASCADE, verbose_name=u'二面面試官')
    second_remark = models.CharField(max_length=135, blank=True, verbose_name=u'專業複試備註')

    # HR终面
    hr_score = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR複試綜合等級')
    hr_responsibility = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR責任心')
    hr_communication_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True,
                                                verbose_name=u'HR坦誠溝通')
    hr_logic_ability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'邏輯思維')
    hr_potential = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR發展潛力')
    hr_stability = models.CharField(max_length=10, choices=HR_SCORE_TYPE, blank=True, verbose_name=u'HR穩定性')
    hr_advantage = models.TextField(max_length=1024, blank=True, verbose_name=u'優勢')
    hr_disadvantage = models.TextField(max_length=1024, blank=True, verbose_name=u'顧慮與不足')
    hr_result = models.CharField(max_length=256, choices=INTERVIEW_RESULT_TYPE, blank=True, verbose_name=u'HR複試結果')
    hr_interviewer_user = models.ForeignKey(User, related_name='hr_interviewer_user', blank=True, null=True,
                                            on_delete=models.CASCADE, verbose_name=u'HR面試官')
    hr_remark = models.CharField(max_length=256, blank=True, verbose_name=u'HR複試備註')

    creator = models.CharField(max_length=256, blank=True, verbose_name=u'複選人數遽創建人')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name=u'創建時間')
    modified_date = models.DateTimeField(auto_now=True, null=True, blank=True, verbose_name=u'更新時間')
    last_editor = models.CharField(max_length=256, blank=True, verbose_name=u'最後編輯者')

    class Meta:
        db_table = u'candidate'
        verbose_name = u'應徵者'
        verbose_name_plural = u'應徵者'

        permissions = [
            ("export", "Can export candidate list"),
            ("notify", "notify interviewer for candidate review"),
        ]

    def __str__(self):
        return self.username
