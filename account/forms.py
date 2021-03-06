from django import forms
from django.contrib.auth.models import User
from .models import Profile

class DateInput(forms.DateInput):
    input_type = 'date'

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    email=forms.EmailField(max_length=65 ,
                           widget=forms.EmailInput)
    username = forms.CharField(max_length=40)
    password = forms.CharField(label='password',
        widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
        widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('first_name',)

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

    def clean_email(self):
        cd = self.cleaned_data
        email=cd['email']

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("این ایمیل قبلا استفاده شده است.")
        return email

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo','bio')
        widgets = {
            'date_of_birth': DateInput(),
        }


class SearchUserForm(forms.Form):
    username = forms.CharField()