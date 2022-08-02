from django.shortcuts import render
from .models import Job
from django.views import generic
from django.views.generic import ListView
from django.shortcuts import render, get_object_or_404


# Create your views here.

class JobList(generic.ListView):
    model = Job
    context_object_name = 'jobs'
    template_name = 'jobs.html'
    queryset = Job.objects.all()

    def get_context_data(self, **kwargs):
        context = super(JobList, self).get_context_data(**kwargs)
        context['topjobs'] = Job.objects.filter(tag__contains='Latestjob').order_by('-post_date')[:4]
        context['top_job'] = Job.objects.filter(tag__contains='Latestjob').order_by('-post_date')[4:8]
        context['latest_job'] = Job.objects.filter(tag__contains='Latestjob').order_by('-post_date')[:25]
        context['admit_card'] = Job.objects.filter(tag__contains='Admitcard').order_by('-post_update')[:25]
        context['results'] = Job.objects.filter(tag__contains='Result').order_by('-post_update')[:25]
        # And so on for more models
        return context

class LatestJob(generic.ListView):
    model = Job
    template_name = 'latest_job.html'
    context_object_name = 'latest_job'
    queryset = Job.objects.filter(tag__contains='Latestjob')

class AdmitCard(generic.ListView):
    model = Job
    template_name = 'admit_card.html'
    context_object_name = 'admit_card'
    queryset = Job.objects.filter(tag__contains='Admitcard')

class Result(generic.ListView):
    model = Job
    template_name = 'jobresult.html'
    context_object_name = 'result'
    queryset = Job.objects.filter(tag__contains='Result')

def job_detail(request, slug):
    template_name = 'job_details.html'
    jobs = get_object_or_404(Job, slug=slug)
    return render(request, template_name, {'jobs': jobs,})
