from django.conf.urls import url, include
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    url(r'^login/', LoginView.as_view(template_name='workshop/workshop_list.html'), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^social/', include('social_django.urls', namespace='social')),
]