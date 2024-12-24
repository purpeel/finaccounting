from django import forms
from costs.spending import models
from costs.spending.models import Spending

class SpendingCreateForm(forms.ModelForm):
    CHOICES = [
        ('Супермаркеты', 'Супермаркеты'), 
        ('Коммунальные платежи, связь, интернет', 'Коммунальные платежи, связь, интернет'),
        ('Погашение кредитов', 'Погашение кредитов'), 
        ('Отдых и развлечения', 'Отдых и развлечения'),
        ('Здоровье и красота', 'Здоровье и красота'),
        ('Транспорт', 'Транспорт'), 
        ('Прочее', 'Прочее')
    ]
    
    price = forms.IntegerField(label='Цена', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    category = forms.ChoiceField(label='Категория', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    account = forms.CharField(label='Название счета', widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    class Meta:
        model = Spending
        fields = [
            'price',
            'category',
            'account'
        ]

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Сумма должна быть больше нуля.")
        return price