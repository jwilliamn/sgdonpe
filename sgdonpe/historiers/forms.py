from django import forms
from sgdonpe.historiers.models import PrincipalStates
from sgdonpe.authentication.models import InternalUser
from django.shortcuts import render
class SelectActivityForm(forms.Form):
    actions = forms.ModelChoiceField(queryset=PrincipalStates.objects.all())


class SelectInternalUserForm(forms.Form):
    users = forms.ModelChoiceField(queryset=InternalUser.objects.all())