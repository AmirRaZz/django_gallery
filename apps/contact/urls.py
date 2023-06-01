from django.urls import path
from . import views

urlpatterns = [
    path('', views.ContactMessageCreateView.as_view(), name='contact'),
    path('contact-success', views.ContactSuccessView.as_view(), name='contact_success'),
]