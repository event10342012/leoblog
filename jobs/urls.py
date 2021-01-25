from django.urls import path

from . import views


def trigger_error(request):
    division_by_zero = 1 / 0


app_name = 'jobs'

urlpatterns = [
    path('', views.get_job_list, name='job_list'),
    path('<int:job_id>/', views.detail, name='jobs'),
    path('resume/add/', views.ResumeCreateView.as_view(), name='resume-add'),
    path('resume/<int:pk>/', views.ResumeDetailView.as_view(), name='resume-detail'),
    path('sentry-debug/', trigger_error),
]
