from django import forms
from .models import AccountModel
JOBS=(('Accountant','Accountant'), ('Engineer','Engineer'),('Software','Software'), ('Designer','Designer'))

class AccountForm(forms.ModelForm):
    class Meta:
        model=AccountModel
        fields=[
            'image',
            'account_bio',
            'user_job',
        ]
        widgets={
            'account_bio':forms.Textarea,
        }
