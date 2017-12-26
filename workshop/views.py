from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from django.utils.functional import cached_property

from .models import Workshop
from .forms import WorkshopForm


class WorkShopListView(ListView):
    model = Workshop

    def dispatch(self, *args, **kwargs):
        print('hello')

        return super(WorkShopListView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.user.is_authenticated:
            workshop_list = Workshop.objects.filter(user=self.request.user)
            context['workshop_list'] = workshop_list
            return context


class WorkshopActionMixin:
    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        pre = form.save(commit=False)
        pre.user = self.request.user
        pre.save()
        messages.info(self.request, self.success_msg)
        return redirect('ws:list')


class WorkshopCreateView(LoginRequiredMixin, WorkshopActionMixin, CreateView):
    model = Workshop
    form_class = WorkshopForm
    success_msg = '作成しました！'


class WorkshopUpdateView(LoginRequiredMixin, WorkshopActionMixin, UpdateView):
    model = Workshop
    form_class = WorkshopForm
    success_msg = '更新しました！'


class WorkshopDetailView(LoginRequiredMixin, DetailView):
    model = Workshop


class WorkshopDeleteView(LoginRequiredMixin, DeleteView):
    model = Workshop

    def get_success_url(self):
        messages.warning(self.request, '削除しました')
        return reverse_lazy('ws:list')

