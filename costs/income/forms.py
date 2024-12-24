from django import forms
from costs.income import models
from costs.income.models import Income

class IncomeCreateForm(forms.ModelForm):
    price = forms.IntegerField(label='Сумма', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    account = forms.CharField(label='Название счёта', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = Income
        fields = [
            'price',
            'account'
        ]

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Сумма должна быть больше нуля.")
        return price


class IncomeAccountCreateForm(forms.ModelForm):
    account = forms.CharField(label='Название счёта', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    goal_title = forms.CharField(label='Цель накопления', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    goal = forms.IntegerField(label='Сумма накопления', required=False, widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    class Meta:
        model = Income
        fields = [
            'account',
            'goal_title',
            'goal'
        ]