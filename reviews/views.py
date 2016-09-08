from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from .models import Questionaire_Review_Model
from .forms import QuestionRatingsForm
from django.contrib.auth.models import User
from django.views.generic import ListView
from user_home.models import AccountModel

#lists all the reviews for the paginator
class Review_List(ListView):
    model=Questionaire_Review_Model
    paginate_by = 10
    template_name = 'reviews/review_pages.html'

    def get_queryset(self, **kwargs):
        user_id=self.kwargs['user']#the user we want to view
        queryset = super(Review_List, self).get_queryset()#lets us get the correct instance
        queryset=Questionaire_Review_Model.objects.filter(user_being_reviewed=User.objects.get(username=user_id))#gets username by id
        return queryset

def pay_to_delete(request,pk):#this deletes a review
    review=Questionaire_Review_Model.objects.select_related('user_being_reviewed').get(pk=pk)
    review.delete()
    account=AccountModel.objects.select_related('user').get(user=request.user)
    diviser=[]
    for i in Questionaire_Review_Model.objects.filter(user_being_reviewed=request.user):#puts all the reviews that have not been deleted into a list
        diviser.append(i.rev)
    try:
        account.user_review=sum(diviser)/len(diviser)#recalculates the user reviews based on ths list
        account.all-=1#subtracts the total user_reviews
    except:
        account.user_review=0#0 if divide by zero occurs
        account.all-=1

    account.save()

    return redirect(reverse('user_home:user_home', kwargs={'user':request.user}))

def reviews(request,user):#the review page that can be made by everyone other than user
    print(AccountModel.objects.filter(user=User.objects.get(username=user)))
    account=AccountModel.objects.select_related('user').get(user=User.objects.get(username=user))
    user_obj=User.objects.get(username=user)
    if request.method == 'POST':
        form=QuestionRatingsForm(request.POST)
        if form.is_valid():
            rating=Questionaire_Review_Model(user_being_reviewed=user_obj)#creates new instance fro the user being reviewed


            #//////////////     Gives us the final score based on the average of the ratings    /////////////////////
            diviser=0
            diviser += int(form.cleaned_data['how'])#put this into a model def to clean it up
            diviser += int(form.cleaned_data['effort'])
            diviser += int(form.cleaned_data['prod'])
            diviser += int(form.cleaned_data['ed'])
            diviser += int(form.cleaned_data['inter'])
            diviser += int(form.cleaned_data['some'])
            diviser /= 6


            #gets the written review and stores in this reviews instance
            rating.written_review=form.cleaned_data['written']


                #the review score for this instance
            rating.rev+=diviser

           #gives us all the reviews for this account so we can check if empty or not
            all=account.all
            all+=1
            account.all=all

                      #adds this instance to the total review points of the user and averages it out
            account.summed_reviews+=rating.rev
            account.user_review=account.summed_reviews/account.all


            account.save()
            rating.save()
            return redirect(reverse('user_home:user_home', kwargs={'user':user}))
    form=QuestionRatingsForm()

    return render(request, 'reviews/reviews.html', {'form':form})

