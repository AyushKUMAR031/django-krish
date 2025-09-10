from django.db import models

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15, unique=True)
    address = models.TextField()
    password = models.CharField(max_length=128)  # Will store hashed password
    profile_photo = models.ImageField(upload_to='profiles/')
    terms_accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.username
