import django_filters
from django import forms
from costs.spending.models import Spending


class LeadEntriesFilter(django_filters.FilterSet):

    CHOICES = [
        ('Супермаркеты', 'Супермаркеты'),
        ('Коммунальные платежи, связь, интернет', 'Коммунальные платежи, связь, интернет'),
        ('Погашение кредитов', 'Погашение кредитов'),
        ('Отдых и развлечения', 'Отдых и развлечения'),
        ('Здоровье и красота', 'Здоровье и красота'),
        ('Транспорт', 'Транспорт'),
        ('Прочее', 'Прочее')
    ]

    start_date = django_filters.DateFilter(field_name='timestamp',
                                           widget=forms.DateInput(
                                               attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
                                           lookup_expr='gte', label='Начальная дата')
    end_date = django_filters.DateFilter(field_name='timestamp',
                                         widget=forms.DateInput(
                                             attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
                                         lookup_expr='lte', label='Конечная дата')
    price = django_filters.CharFilter(label='Сумма')
    category = django_filters.ChoiceFilter(label='Категория', choices=CHOICES, widget=forms.Select(attrs={'class': 'form-select'}))
    account = django_filters.CharFilter(label='Счёт')

    # account_nummer = django_filters.

    class Meta:
        model = Spending
        fields = ['start_date', 'end_date', 'price', 'category', 'account']

    @property
    def qs(self):
        parent = super().qs
        return parent.order_by('-timestamp')


class AccountsFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(label='Сумма')
    account = django_filters.CharFilter(label='Счёт')
    class Meta:
        model = Spending
        fields = [
            'price',
            'account'
        ]

    @property
    def qs(self):
        parent = super().qs

        return parent.order_by('account')