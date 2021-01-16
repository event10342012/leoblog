# Generated by Django 3.1.5 on 2021-01-16 03:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'permissions': [('export', 'Can export candidate list'), ('notify', 'notify interviewer for candidate review')], 'verbose_name': '應徵者', 'verbose_name_plural': '應徵者'},
        ),
        migrations.AlterField(
            model_name='candidate',
            name='apply_position',
            field=models.CharField(blank=True, max_length=135, verbose_name='應徵職位'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='bachelor_school',
            field=models.CharField(blank=True, max_length=135, verbose_name='大學學校'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='born_address',
            field=models.CharField(blank=True, max_length=135, verbose_name='出生地'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='candidate_remark',
            field=models.CharField(blank=True, max_length=135, verbose_name='備註'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='創建時間'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='creator',
            field=models.CharField(blank=True, max_length=256, verbose_name='複選人數遽創建人'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='degree',
            field=models.CharField(blank=True, choices=[('本科', '本科'), ('硕士', '硕士'), ('博士', '博士')], max_length=135, verbose_name='學歷'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='doctor_school',
            field=models.CharField(blank=True, max_length=135, verbose_name='博士學校'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='email',
            field=models.EmailField(blank=True, max_length=135, verbose_name='郵箱'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_advantage',
            field=models.TextField(blank=True, max_length=1024, verbose_name='優勢'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_disadvantage',
            field=models.TextField(blank=True, max_length=1024, verbose_name='顧慮與不足'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='first_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='面試官'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_learning_ability',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='學習能力得分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_professional_competency',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='專業能力得分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_recommend_position',
            field=models.CharField(blank=True, max_length=256, verbose_name='推薦部門'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_remark',
            field=models.CharField(blank=True, max_length=135, verbose_name='初試備註'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_result',
            field=models.CharField(blank=True, choices=[('建议复试', '建议复试'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='初試結果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='first_score',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='1-5分，極優秀: >=4.5，優秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，較差: <3分', max_digits=2, null=True, verbose_name='初试分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='gender',
            field=models.CharField(blank=True, max_length=135, verbose_name='性別'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_advantage',
            field=models.TextField(blank=True, max_length=1024, verbose_name='優勢'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_communication_ability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR坦誠溝通'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_disadvantage',
            field=models.TextField(blank=True, max_length=1024, verbose_name='顧慮與不足'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hr_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='HR面試官'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_logic_ability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='邏輯思維'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_potential',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR發展潛力'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_remark',
            field=models.CharField(blank=True, max_length=256, verbose_name='HR複試備註'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_responsibility',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR責任心'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_result',
            field=models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='HR複試結果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_score',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR複試綜合等級'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='hr_stability',
            field=models.CharField(blank=True, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')], max_length=10, verbose_name='HR穩定性'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='last_editor',
            field=models.CharField(blank=True, max_length=256, verbose_name='最後編輯者'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='major',
            field=models.CharField(blank=True, max_length=135, verbose_name='專業'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='master_school',
            field=models.CharField(blank=True, max_length=135, verbose_name='研究所學校'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='modified_date',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='更新時間'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='paper_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='筆試成績'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='phone',
            field=models.CharField(max_length=135, verbose_name='手機號碼'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_advantage',
            field=models.TextField(blank=True, max_length=1024, verbose_name='優勢'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_communication_ability',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='溝通能力得分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_disadvantage',
            field=models.TextField(blank=True, max_length=1024, verbose_name='顧慮與不足'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_interviewer_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='second_interviewer_user', to=settings.AUTH_USER_MODEL, verbose_name='二面面試官'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_learning_ability',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='學習能力得分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_pressure_score',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='抗壓能力得分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_professional_competency',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True, verbose_name='專業能力得分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_recommend_position',
            field=models.CharField(blank=True, max_length=256, verbose_name='建議方向或推薦部門'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_remark',
            field=models.CharField(blank=True, max_length=135, verbose_name='專業複試備註'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_result',
            field=models.CharField(blank=True, choices=[('建议录用', '建议录用'), ('待定', '待定'), ('放弃', '放弃')], max_length=256, verbose_name='專業複試結果'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='second_score',
            field=models.DecimalField(blank=True, decimal_places=1, help_text='1-5分，極優秀: >=4.5，優秀: 4-4.4，良好: 3.5-3.9，一般: 3-3.4，較差: <3分', max_digits=2, null=True, verbose_name='專業複試得分'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='test_score_of_general_ability',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, verbose_name='綜合能力評測成績'),
        ),
        migrations.AlterField(
            model_name='candidate',
            name='userid',
            field=models.IntegerField(blank=True, null=True, unique=True, verbose_name='應徵者ID'),
        ),
    ]