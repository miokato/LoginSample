from django.views.generic import FormView, TemplateView
from django.shortcuts import redirect

from .models import Machine
from .forms import MachineForm


class MachineRegisterView(FormView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine/register.html'
    success_url = '/machine/confirm/'

    def form_valid(self, form):
        self.request.session['form_data'] = form.cleaned_data
        return super().form_valid(form)


class MachineConfirmView(FormView):
    model = Machine
    form_class = MachineForm
    template_name = 'machine/confirm.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_data'] = self.request.session['form_data']
        return context

    def post(self, request, *args, **kwargs):
        form_data = request.session.pop('form_data', None)

        machine = Machine()
        machine.name = form_data['name']
        machine.color = form_data['color']
        machine.save()
        return redirect('machine:thanks')


class MachineThanksView(TemplateView):
    template_name = 'machine/thanks.html'

