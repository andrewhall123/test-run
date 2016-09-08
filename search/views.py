from django.shortcuts import render
from .forms import FilterForm
from django.contrib.auth.models import User
from user_home.models import AccountModel
from reviews.models import Questionaire_Review_Model

def search(request):

    form=FilterForm()
    return_obj=filter(request)
    return render(request, 'search/search_results.html',
                  {'ret_obj': return_obj})

def filter(request):
    if request.method=='GET':
        form=FilterForm(request.GET['filt'])
        #if form.is_valid():
        search_bar=request.GET.get('q')
        filt=request.GET.get('filt')
        user_obj=''
        filt_by_jobs=''
        filt_by_review=''
        user=returnable=[i for i in User.objects.all() if i.username.lower().find(search_bar.lower())!=-1]
        job=[i.user.username for i in AccountModel.objects.all() if i.user_job.lower().find(search_bar.lower())!=-1]
        if filt.lower() == 'user':
            returnable=user
        elif filt.lower()=='job':
            returnable=job
        else:
            returnable=user+job

        return returnable