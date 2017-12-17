from django.shortcuts import render
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.core.urlresolvers import reverse_lazy
from .models import Workshop
from .forms import WorkshopForm


class WorkShopListView(ListView):
    template_name = 'workshop/workshop_list.html'
    model = Workshop

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        if self.request.user.is_authenticated:
            workshop_list = Workshop.objects.filter(user=self.request.user)
            context['workshop_list'] = workshop_list
            return context


class WorkshopDetailView(LoginRequiredMixin, DetailView):
    template_name = 'workshop/workshop_detail.html'
    model = Workshop


class WorkshopCreateView(LoginRequiredMixin, CreateView):
    template_name = 'workshop/workshop_form.html'
    model = Workshop
    form_class = WorkshopForm

    def form_valid(self, form):
        pre = form.save(commit=False)
        pre.user = self.request.user
        pre.save()
        messages.info(self.request, '作成しました')
        return redirect('ws:list')


class WorkshopUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'workshop/workshop_form.html'
    model = Workshop
    form_class = WorkshopForm

    def get_success_url(self):
        messages.info(self.request, '更新しました')
        return reverse_lazy('ws:list')


class WorkshopDeleteView(LoginRequiredMixin, DeleteView):
    model = Workshop

    def get_success_url(self):
        messages.warning(self.request, '削除しました')
        return reverse_lazy('ws:list')

