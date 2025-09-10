from django import forms
from django.core.exceptions import ValidationError

def validate_password_strength(value):
    if len(value) < 12:
        raise ValidationError("Password must be at least 12 characters long.")

# Step 1 form
class UserForm(forms.Form):
    username = forms.CharField(max_length=150)
    email = forms.EmailField()
    phone = forms.CharField(max_length=15)

# Step 2 form
class AddressPasswordForm(forms.Form):
    address = forms.CharField(widget=forms.Textarea)
    password = forms.CharField(widget=forms.PasswordInput, validators=[validate_password_strength])
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("password")
        cpwd = cleaned_data.get("confirm_password")
        if pwd and cpwd and pwd != cpwd:
            raise ValidationError("Passwords do not match.")
        return cleaned_data

# Step 3 form
class ProfilePhotoConsentForm(forms.Form):
    profile_photo = forms.ImageField()
    terms_accepted = forms.BooleanField()

    def clean_profile_photo(self):
        photo = self.cleaned_data['profile_photo']
        if photo.size > 5 * 1024 * 1024:  # 5MB
            raise ValidationError("Profile photo must be less than 5MB.")
        return photo
