from django.shortcuts import render

from jobs.models import Job, job_types, cites


# Create your views here.


def get_job_list(request):
    job_list = Job.objects.order_by('job_type')
    context = {'job_list': job_list}
    for job in job_list:
        job.city_name = cites[job.job_city][1]
        job.type_name = job_types[job.job_type][1]
    return render(request, 'jobs/job_list.html', context)
