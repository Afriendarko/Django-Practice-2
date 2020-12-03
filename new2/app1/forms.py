from django import forms
from .models import feedback

class NameForm(forms.Form):
    Your_Name= forms.CharField(label="Your_Name", max_length=20)
    Email= forms.EmailField(label="Email_Field", max_length=20)

class feedbackform(forms.ModelForm):
    class Meta:
        model = feedback
        fields = "__all__"

# class CustomUserCreationForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = "__all__"