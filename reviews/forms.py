from django import forms


CHOICES=((1,'1'), (2,'2'), (3,'3'),(4,'4'))

class QuestionRatingsForm(forms.Form):
    how = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.RadioSelect, initial=4, label='Hoew')
    effort = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.RadioSelect, initial=3, label='Effort')
    prod = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.RadioSelect, initial=1, label='Productivity')
    ed = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.RadioSelect, initial=3, label='Education')
    inter = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.RadioSelect, initial=2,
                              label='Interpersonal')
    some = forms.ChoiceField(required=True, choices=CHOICES, widget=forms.RadioSelect, initial=3,
                             label='Some other Question')
    written=forms.CharField(widget=forms.Textarea, label='Comments (optional)', required=False, initial=None)
