from django.shortcuts import render
from django.contrib.auth.models import User
from user_home.models import AccountModel
from django.views.generic import ListView
from django.views.decorators.cache import cache_page


class employee(ListView):
    model=AccountModel.objects.all().order_by('-user_review')
    paginate_by = 10
    template_name = 'employees/employ.html'

def employee_by_review(request):
    review_stats=AccountModel.objects.all().order_by('-user_review')
    return render(request,'employees/employ.html', {'users':review_stats})