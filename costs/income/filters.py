import django_filters
from django import forms
from costs.income.models import Income


class LeadEntriesFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name='timestamp',
                                           widget=forms.DateInput(
                                               attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
                                           lookup_expr='gte', label='Начальная дата')
    end_date = django_filters.DateFilter(field_name='timestamp',
                                         widget=forms.DateInput(
                                             attrs={'class': 'form-control form-control-lg', 'type': 'date'}),
                                         lookup_expr='lte', label='Конечная дата')
    price = django_filters.CharFilter(label='Сумма')
    account = django_filters.CharFilter(label='Счёт')
    class Meta:
        model = Income
        fields = ['start_date', 'end_date', 'price','account']

    @property
    def qs(self):
        parent = super().qs

        return parent.order_by('-timestamp')


class AccountsFilter(django_filters.FilterSet):
    price = django_filters.CharFilter(label='Сумма')
    account = django_filters.CharFilter(label='Счёт')
    class Meta:
        model = Income
        fields = [
            'price',
            'account'
        ]

    @property
    def qs(self):
        parent = super().qs
        return parent.order_by('account')


class BalanceFilter(django_filters.FilterSet):
    sum = django_filters.CharFilter(label='Сумма')
    account = django_filters.CharFilter(label='Счёт')
    goal = django_filters.CharFilter(label='Цель')
    goal_title = django_filters.CharFilter(label='Сумма накопления')
    class Meta:
        model = Income
        fields = [
            'price',
            'account',
            'goal',
            'goal_title'
        ]

    @property
    def qs(self):
        parent = super().qs
        return parent.order_by('account')

