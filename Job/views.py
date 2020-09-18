from django.shortcuts import redirect ,render
from .models import job
from django.core.paginator import Paginator
from .form import applyform , jobform
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .filters import JobFilter

# Create your views here.

def job_list(request):
    job_list = job.objects.all()
    ## filters
    myfilters = JobFilter(request.GET,queryset=job_list)
    
    job_list = myfilters.qs

    paginator = Paginator(job_list, 3) # Show 'no.' contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    
    context = {'jobs': page_obj, 'myfilters':myfilters } #template name 
    return render(request,'job/job_list.html',context)



@login_required
def job_detail(request, slug):
    job_detail = job.objects.get(slug=slug)

    if request.method =='POST':
        form = applyform(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.job = job_detail
            myform.save()
            
    else:
        form = applyform()

    context = {'job':job_detail, 'form':form}
    return render(request,'job/job_detail.html',context)


@login_required
def add_job(request):
    if request.method =='POST':
        form = jobform(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = jobform()
    
    return render(request, 'job/add_job.html',{'form':form})