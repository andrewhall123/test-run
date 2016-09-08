from django.db import models
from django.contrib.auth.models import User
from user_home.models import AccountModel
from django.contrib.postgres.fields import HStoreField

CHOICES=((1,'1'), (2,'2'), (3,'3'),(4,'4'))

class Questionaire_Review_Model(models.Model):
    #the review score for this model
    rev=models.FloatField(choices=CHOICES, default=0, null=True)

    #the user being reviewed
    user_being_reviewed=models.ForeignKey(User, null=True,blank=True)

    #the image used for the all employees page
    image=models.ImageField(upload_to='documents/%Y/%m/%d',null=True, blank=True,  default=None)

    #the written review for this instance
    written_review=models.CharField(null=True, max_length=2000, default=None)

    try:
        picture=AccountModel.objects.get(user=user_being_reviewed).image
    except:
        picture=None
    def get_all(self):
        return self.all

