from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(max_length=40)
    password = forms.CharField(label='password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("پسورد های وارد شده با یکدیگر مغایرت دارند")

    def clean_username(self):
        cd = self.cleaned_data
        username=cd['username']
        # try:
        #     user = User.objects.get(username=cd['username'])
        # except User.DoesNotExist:
        #     return username
        # raise forms.ValidationError("نام کاربری قبلا انتخاب شده است. لطفا نام کاربری دیگری انتخاب کنید")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("نام کاربری قبلا انتخاب شده است. لطفا نام کاربری دیگری انتخاب کنید")
        return username

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')