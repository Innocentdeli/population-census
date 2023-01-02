from django import forms

class censusRegistrationAndUpdateForm(forms.Form):
    firstname = forms.CharField(label='First Name', max_length=225)
    lastname = forms.CharField(label='Last Name', max_length=225)
    age = forms.IntegerField(label='Age' )
    gender = forms.CharField(label='Gender', max_length=3)

