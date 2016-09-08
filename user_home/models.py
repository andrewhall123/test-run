from __future__ import unicode_literals
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import HStoreField, ArrayField

JOBS=(('Accountant','Accountant'), ('Engineer','Engineer'),('Software','Software'), ('Designer','Designer'))

class AccountManager(models.Manager):
    def create_account(self, user):
        account=self.create(user=user)

class AccountModel(models.Model):
    #the image file
    image=models.ImageField(upload_to='documents/%Y/%m/%d',null=True, blank=True,  default=None)

    #user associated with account
    user=models.ForeignKey(User, blank=True,null=True, on_delete=models.CASCADE, related_name='user')

    #the account bio
    account_bio=models.CharField(max_length=2000, null=True, blank=True, default=None)

    #the user's job
    user_job=models.CharField(choices=JOBS, null=True, max_length=25)

    #the total score of the user
    user_review=models.FloatField(default=0.0)

    #a manager to help with creation
    objects=AccountManager()

    #the viewer viewing this account's page
    viewer=models.ForeignKey(User, null=True, related_name='viewer')


    #total amount of reviews
    all=models.IntegerField(default=0, null=True)

    #total points of all reviews
    summed_reviews=models.FloatField(default=0.0, null=True)

    def get_view_user_account(self, request):#check to see if user has info or not, and create instance if first login
        try:
            account=AccountModel.objects.select_related('user').get(user=request.user)
            return account
        except:
            account=AccountModel(user=request.user)
            account.save()
            return account

    def get_actual_user(self, user):
        try:
            account=AccountModel.objects.select_related('user').get(user=User.objects.get(username=user))
        except:
            account=AccountModel(user=User.objects.get(username=user))

    def is_empty(self):
        if self.image is None:
            return True
        else:
            return False


#just the job list
class Job_List(models.Model):
    accountant=models.IntegerField(default=0)
    engineer=models.IntegerField(default=0)
    designer = models.IntegerField(default=0)
    software = models.IntegerField(default=0)

    #dictionary object to help with mapping
    datas=HStoreField(max_length=2000, null=True)


