from formtools.wizard.views import SessionWizardView
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

from .forms import UserForm, AddressPasswordForm, ProfilePhotoConsentForm

file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'temp'))

FORMS = [
    ("user", UserForm),
    ("address_pwd", AddressPasswordForm),
    ("photo_terms", ProfilePhotoConsentForm),
]

TEMPLATES = {
    "0": "step1.html",
    "1": "step2.html",
    "2": "step3.html",
}

def Me(request):
    return render(request, 'land.html')

class UserRegistrationWizard(SessionWizardView):
    form_list = FORMS
    file_storage = file_storage  # <--- add this

    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        data = {}
        for form in form_list:
            data.update(form.cleaned_data)

        return render(self.request, "done.html", {"data": data})
