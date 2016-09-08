from django import forms

FILTER=(('----','----'),('User','User'), ('Job', 'Job'))

class FilterForm(forms.Form):
    filt=forms.ChoiceField(choices=FILTER)