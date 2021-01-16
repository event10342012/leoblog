from django.http import Http404
from django.shortcuts import render

from jobs.models import Job, job_types, cites


# Create your views here.


def get_job_list(request):
    job_list = Job.objects.order_by('job_type')
    context = {'job_list': job_list}
    for job in job_list:
        job.city_name = cites[job.job_city][1]
        job.type_name = job_types[job.job_type][1]
    return render(request, 'jobs/joblist.html', context)


def detail(request, job_id):
    try:
        job = Job.objects.get(pk=job_id)
        job.city_name = cites[job.job_city][1]
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'jobs/job.html', {'job': job})
