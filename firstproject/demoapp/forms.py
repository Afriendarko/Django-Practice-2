from django import forms

class NameForm(forms.Form):
    Your_Name= forms.CharField(label="Your_Name", max_length=20)
    Email= forms.EmailField(label="Email_Field", max_length=20)