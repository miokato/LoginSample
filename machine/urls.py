from django.conf.urls import url
from .views import MachineRegisterView, MachineConfirmView, MachineThanksView


urlpatterns = [
    url(r'^$', MachineRegisterView.as_view(), name='register'),
    url(r'^confirm/', MachineConfirmView.as_view(), name='confirm'),
    url(r'^thanks/', MachineThanksView.as_view(), name='thanks'),
]