from django import forms
from user.models import User
from user.utils import *
from django.contrib.auth.hashers import check_password


class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'})
        }

    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Repeat Password'}))

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match.')
        if not validate_password(password2):
            raise forms.ValidationError(ERROR_MESSAGE)
        return password2

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Email'}))
    password = forms.CharField(
        label='Pasword',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Password'}))


class ChangePasswordForm(forms.ModelForm):
    class Meta:
        model = User
        fields = []

    old_password = forms.CharField(label='Password',
                                   widget=forms.PasswordInput(
                                       attrs={'class': 'form-control',
                                              'placeholder': 'Old Password'
                                              }))
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'New Password'
                                           }))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': 'form-control',
                                           'placeholder': 'Repeat New Password'
                                           }))

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        user_password = self.instance.password
        if not check_password(old_password, user_password):
            raise forms.ValidationError('You have entered wrong password!')

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Passwords don\'t match!')
        if not validate_password(password2):
            raise forms.ValidationError(ERROR_MESSAGE)
        return password2

    def save(self, commit=True):
        user = super(ChangePasswordForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


