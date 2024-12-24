from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from costs.income.forms import *
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from costs.users.mixins import RightUserMixin
from costs.income.mixins import AuthorAccessMixin
from costs.income.models import *
from costs.spending.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from costs.income.filters import *
from datetime import date
from costs.income.func import *
from costs.spending.func import summarize as spending_sum
from costs.spending.filters import AccountsFilter as SpendingFilter


class IncomeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('users:login')
    success_message = 'Запись добавлена'
    template_name = 'income/create.html'
    form_class = IncomeCreateForm
    success_url = reverse_lazy('income:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class IncomeAccountCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('users:login')
    success_message = 'Цель отредактирована'
    template_name = 'income/create_goal.html'
    form_class = IncomeAccountCreateForm
    success_url = reverse_lazy('income:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IncomeUpdateView(AuthorAccessMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    success_message = 'Запись изменена'
    template_name = 'income/update.html'
    form_class = IncomeCreateForm
    success_url = reverse_lazy('income:index')
    model = Income


class IncomeDeleteView(AuthorAccessMixin, SuccessMessageMixin, DeleteView):
    model = Income
    template_name = 'Income/delete.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('income:index')
    success_message = 'Запись удалена'


class IndexIncomesView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')
    def get(self, request, *args, **kwargs):
        filter1 = LeadEntriesFilter(request.GET, queryset=Income.objects.filter(author=request.user))
        d1 = prepare(filter1.qs)
        labels, data = list(d1.keys()), list(d1.values())

        filter2 = AccountsFilter(request.GET, queryset=Income.objects.filter(author=request.user))
        d2 = summarize(filter2.qs)

        filter3 = SpendingFilter(request.GET, queryset=Spending.objects.filter(author=request.user))
        d3 = spending_sum(filter3.qs)
        d = balances(d2, d3)

        filter4 = BalanceFilter(request.GET, queryset=Income.objects.filter(author=request.user))
        d4 = parser(filter4.qs, filter3.qs)

        return render(request, 'income/index.html', {'filter1': filter1, 'labels': labels,
                                                     'data': data, 'd': d, 'd1': d4})