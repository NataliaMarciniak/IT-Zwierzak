from django import forms

class Adoption(forms.Form):
    education = forms.CharField(label="education", max_length=250)