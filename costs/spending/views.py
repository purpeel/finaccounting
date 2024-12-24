from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from costs.spending.forms import *
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from costs.users.mixins import RightUserMixin
from costs.spending.mixins import AuthorAccessMixin
from costs.spending.models import *
from django.contrib.auth.mixins import LoginRequiredMixin
from costs.spending.filters import *
from datetime import date
from costs.spending.func import *


class SpendingCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    login_url = reverse_lazy('users:login')
    success_message = 'Трата добавлена'
    template_name = 'spending/create.html'
    form_class = SpendingCreateForm
    success_url = reverse_lazy('spending:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class SpendingUpdateView(AuthorAccessMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('users:login')
    success_message = 'Трата изменена'
    template_name = 'spending/update.html'
    form_class = SpendingCreateForm
    success_url = reverse_lazy('spending:index')
    model = Spending


class SpendingDeleteView(AuthorAccessMixin, SuccessMessageMixin, DeleteView):
    model = Spending
    template_name = 'spending/delete.html'
    login_url = reverse_lazy('users:login')
    success_url = reverse_lazy('spending:index')
    success_message = 'Трата удалена'


class IndexSpendingsView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        filter1 = LeadEntriesFilter(request.GET, queryset=Spending.objects.filter(author=request.user))
        d1 = prepare(filter1.qs)
        labels, data = list(d1.keys()), list(d1.values())
        filter2 = AccountsFilter(request.GET, queryset=Spending.objects.filter(author=request.user))
        d2 = summarize(filter2.qs)
        return render(request, 'spending/index.html', {'filter1': filter1, 'labels': labels,
                                                     'data': data, 'd2': d2})


class CircleDiagramView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        author = request.user
        date_now = date.today()
        if date_now.month == 1:
            date_old = date(date_now.year - 1, 12, 1)
        else:
            date_old = date(date_now.year, date_now.month - 1, 1)

        qs_now = Spending.objects.filter(author=author).filter(timestamp__year=date_now.year,
                                                               timestamp__month=date_now.month)
        qs_old = Spending.objects.filter(author=author).filter(timestamp__year=date_old.year,
                                                               timestamp__month=date_old.month)

        d_now = prepare(qs_now)
        d_old = prepare(qs_old)

        labels_now, labels_old = list(d_now.keys()), list(d_old.keys())
        data_now, data_old = list(d_now.values()), list(d_old.values())

        return render(request, 'spending/diagram.html', {'labels_now': labels_now, 'data_now': data_now,
                                                         'labels_old': labels_old, 'data_old': data_old})


class CircleDefinView(LoginRequiredMixin, View):
    login_url = reverse_lazy('users:login')

    def get(self, request, *args, **kwargs):
        f = LeadEntriesFilter(request.GET, queryset=Spending.objects.filter(author=request.user))
        d = prepare(f.qs)
        labels, data = list(d.keys()), list(d.values())
        return render(request, 'spending/diagram_date.html', {'f': f, 'labels': labels, 'data': data})
