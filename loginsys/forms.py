from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# 28.05.2016
#from django.utils.safestring import mark_safe
class UserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # 28.05.2016
    #my_field = forms.CharField(label=mark_safe('<br />'))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        #user = super(UserCreateForm, self).save(commit=False)
        user = super(UserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user