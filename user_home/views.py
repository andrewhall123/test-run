from django.shortcuts import render
from .models import AccountModel, Job_List
from reviews.models import Questionaire_Review_Model
from .forms import AccountForm
from django.contrib.auth.models import User

def user_home(request, user):
    user=User.objects.get(username=user)
    # gets the user account that the page belongs to
    try:
        account = AccountModel.objects.select_related('user').get(user=user)
    except:
        account=AccountModel(user=user)



    # gets the viewer's user name so he does not have certain priveleges and so he can make reviews
    account.viewer = User.objects.get(username=request.user)


    account.save()
    return form_check(request, account)


# what the page actually displays
def display(request, account, account_form):
    """i=AccountModel.objects.all()
    a=Job_List.objects.all()
    q=Questionaire_Review_Model.objects.all()
    q.delete()
    i.delete()
    a.delete()"""

    #Gets all the jobs for the website and how many of each
    try:
        job=Job_List.objects.get(pk=0)
    except:
        job=Job_List(pk=0)
        job.datas={'Accountant':0,'Engineer':0,'Designer':0, 'Software':0}
        job.save()



    return render(request, 'user_home/user_home.html', {'account': account, 'account_form': account_form, 'job_stats':job.datas,
                                                        'review_short':Questionaire_Review_Model.objects.filter(user_being_reviewed=account.user)[:3]})


def form_check(request, account):
    #the  "about me" form will appear if the user clicks on the edit account button, or if this is the first time they sign in
    if request.GET.get('edit_image') is not None or account.user_job is None:
        account=AccountModel.objects.select_related('user').get(user=account.viewer)

        #the initial refers to the bio so it stays in the form
        account_form = AccountForm(initial={'account_bio': account.account_bio, 'user_job':account.user_job})
        return edit(request, account, account_form)
    else:
        account_form = None
        return display(request,account,account_form)


def travers(request,user):
    account=AccountModel.objects.select_related('user').get(user=request.user)
    account_form=None
    return edit(request,account,account_form)

def edit(request, account, account_form):
    if request.method == 'POST':
        account_form = AccountForm(request.POST, request.FILES)#gets all the form's info
        if account_form.is_valid():
            account_job=account.user_job
            image=request.FILES.get('image')
            clean=account_form.cleaned_data['account_bio']

            account.account_bio = clean


            #if user already has an image then he does not have to re upload everytime he makes an edit
            if image is not None:
                account.image=image

            else:
                account.image=account.image

            #gets the job
            job=request.POST.get('user_job')

            #the job to subtract is not none only if the user changed their jobs in order to keep calculations correct
            job_to_subtract=None
            if account_job is not None:
                job_to_subtract=account_job
                print(account_job)
            if account_job==job:
                account_form=None
                return render(request, 'user_home/user_home.html', {'account': account,
                                                                    'account_form': account_form,
                                                                    'job_stats': Job_List.objects.get(pk=0).datas})
            account.user_job=job
            account.save()
            try:
                jobl = Job_List.objects.get(pk=0)
            except:
                jobl = Job_List(pk=0)
                job.datas={'Accountant':0,'Engineer':0,'Designer':0, 'Software':0}
            if job_to_subtract is not None:
                temp=int(jobl.datas[job_to_subtract])-1
                jobl.datas[job_to_subtract]=temp

                temp=int(jobl.datas[job])+1
                jobl.datas[job]=temp
            else:
                jobl.datas[job] = int(jobl.datas[job]) + 1
            jobl.save()
            account_form=None
            return render(request, 'user_home/user_home.html', {'account':account,
                                                                'account_form':account_form,
                                                                'job_stats': Job_List.objects.get(pk=0).datas})
    return render(request, 'user_home/user_home.html', {'account': account,
                                                        'account_form': account_form,
                                                        'job_stats': Job_List.objects.get(pk=0).datas})

