from django.urls import path
from .views import UserRegistrationWizard
from .forms import UserForm, AddressPasswordForm, ProfilePhotoConsentForm
from . import views

urlpatterns = [
    path('', views.Me, name='me'),
    path('register/', UserRegistrationWizard.as_view([UserForm, AddressPasswordForm, ProfilePhotoConsentForm]), name='user_register'),
]