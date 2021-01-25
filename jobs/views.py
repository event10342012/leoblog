import logging

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, DetailView

from jobs.models import Job, job_types, cites, Resume


# Create your views here.
logging.getLogger(__name__)

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
        logging.info('job info fetch from db')
    except Job.DoesNotExist:
        raise Http404("Job does not exist")
    return render(request, 'jobs/job.html', {'job': job})


class ResumeCreateView(LoginRequiredMixin, CreateView):
    """簡歷職位頁面"""
    template_name = 'jobs/resume_form.html'
    success_url = '/jobs/'
    model = Resume
    fields = ["username", "city", "phone",
              "email", "apply_position", "gender",
              "bachelor_school", "master_school", "major", "degree", "picture", "attachment",
              "candidate_introduction", "work_experience", "project_experience"]

    def get_initial(self):
        initial = {}
        for x in self.request.GET:
            initial[x] = self.request.GET[x]
        return initial

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.applicant = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class ResumeDetailView(DetailView):
    model = Resume
    template_name = 'jobs/resume_detail.html'
