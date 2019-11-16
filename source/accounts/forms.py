
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class UserCreationForm(forms.ModelForm):
    password = forms.CharField(label="Пароль", strip=False, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label="Подтвердите пароль", widget=forms.PasswordInput, strip=False)

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError('Пароли не совпадают!')
        return password_confirm

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password', 'password_confirm', 'first_name', 'last_name', 'email']


# class SignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True, label='Email')
#
#     class Meta(UserCreationForm.Meta):
#         fields = ('username', 'email')
#
#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         try:
#             User.objects.get(email=email)
#             raise ValidationError('Email already registered.', code='email_registered')
#         except User.DoesNotExist:
#             return email