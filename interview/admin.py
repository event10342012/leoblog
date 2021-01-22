import csv
from datetime import datetime

from django.contrib import admin
from django.db.models import Q
from django.http import HttpResponse
from django.utils.safestring import mark_safe

from interview import candidate_field as cf
from interview.models import Candidate
from jobs.models import Resume

# Register your models here.

exportable_fields = (
    'username', 'city', 'phone', 'bachelor_school', 'master_school', 'degree', 'first_result', 'first_interviewer_user',
    'second_result', 'second_interviewer_user', 'hr_result', 'hr_score', 'hr_remark', 'hr_interviewer_user')


def export_model_as_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type='text/csv')
    field_list = exportable_fields
    today = datetime.now().strftime('%Y-%m-%d_%H%M%S')
    response['content-disposition'] = f'attachment; filename=recruitment-candidates-list-{today}.csv'

    writer = csv.writer(response)
    writer.writerow(
        [queryset.model._meta.get_field(f).verbose_name.title() for f in field_list]
    )

    for obj in queryset:
        csv_line_values = []
        for filed in field_list:
            field_obj = queryset.model._meta.get_field(filed)
            field_value = field_obj.value_from_object(obj)
            csv_line_values.append(field_value)
        writer.writerow(csv_line_values)

    return response


export_model_as_csv.short_description = '輸出csv檔案'
export_model_as_csv.allowed_permissions = ('export',)


class CandidateAdmin(admin.ModelAdmin):
    exclude = ('creator', 'created_date', 'modified_date')

    actions = [export_model_as_csv]

    list_display = (
        'username', 'city', 'bachelor_school', 'get_resume', 'first_score', 'first_result', 'first_interviewer_user',
        'second_result', 'second_interviewer_user', 'hr_score', 'hr_result', 'last_editor',)

    # 搜尋欄位
    search_fields = ('username', 'phone', 'email', 'bachelor_school')

    # 篩選條件
    list_filter = (
        'city', 'first_result', 'second_result', 'hr_result', 'first_interviewer_user', 'second_interviewer_user',
        'hr_interviewer_user')

    # 排序欄位
    ordering = ('hr_result', 'second_result', 'first_result')

    def get_resume(self, obj):
        if not obj.phone:
            return ""
        resumes = Resume.objects.filter(phone=obj.phone)
        if resumes and len(resumes) > 0:
            return mark_safe(u'<a href="/jobs/resume/%s" target="_blank">%s</a' % (resumes[0].id, "查看簡歷"))
        return ""

    def has_export_permission(self, request):
        opts = self.opts
        return request.user.has_perm(f'{opts.app_label}.export')

    # 对于非管理员，非HR，获取自己是一面面试官或者二面面试官的候选人集合:s
    def get_queryset(self, request):  # show data only owned by the user
        qs = super(CandidateAdmin, self).get_queryset(request)

        group_names = self.get_group_names(request.user)
        if request.user.is_superuser or 'hr' in group_names:
            return qs
        return Candidate.objects.filter(
            Q(first_interviewer_user=request.user) | Q(second_interviewer_user=request.user))

    def get_fieldsets(self, request, obj=None):
        group_names = self.get_group_names(request.user)

        if 'interviewer' in group_names and obj.first_interviewer_user == request.user:
            return cf.default_fieldsets_first
        if 'interviewer' in group_names and obj.second_interviewer_user == request.user:
            return cf.default_fieldsets_second
        return cf.default_fieldsets

    def save_model(self, request, obj, form, change):
        obj.last_editor = request.user.username
        if not obj.creator:
            obj.creator = request.user.username
        obj.modified_date = datetime.now()
        obj.save()

    def get_group_names(self, user):
        group_names = []
        for g in user.groups.all():
            group_names.append(g.name)
        return group_names

    def get_readonly_fields(self, request, obj=None):
        group_names = self.get_group_names(request.user)

        if 'interviewer' in group_names:
            return 'first_interviewer_user', 'second_interviewer_user'
        return ()

    def get_list_editable(self, request):
        group_names = self.get_group_names(request.user)

        if request.user.is_superuser or 'hr' in group_names:
            return 'first_interviewer_user', 'second_interviewer_user'
        return {}

    def get_changelist_instance(self, request):
        """
        override admin method and list_editable property value
        with values returned by our custom method implementation.
        """
        self.list_editable = self.get_list_editable(request)
        return super(CandidateAdmin, self).get_changelist_instance(request)


admin.site.register(Candidate, CandidateAdmin)
