from django import forms

from .models import UserRegistration, Referral


class RegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = ('name', 'age', 'city')


class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ('name', 'age', 'city')
