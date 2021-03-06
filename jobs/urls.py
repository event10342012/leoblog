from django.urls import path

from . import views

app_name = 'jobs'

urlpatterns = [
    path('', views.get_job_list, name='job_list'),
    path('<int:job_id>/', views.detail, name='jobs')
]
