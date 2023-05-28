from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError
# import magic

# To check the extension of the file uploaded so that only audio files are uploaded using extension
ext_validator = FileExtensionValidator(['mp3', 'wav', 'flac'])

# Commenting out because deploying with python-magic-bin doesnt work.
# Check the file content using python-magic so that only audio files are uploaded
# def validate_file_mimetype(file):
#     accept = ['audio/mpeg', 'audio/wav', 'audio/flac', 'audio/x-wav']
#     file_mime_type = magic.from_buffer(file.read(1024), mime=True)

#     if file_mime_type not in accept:
#         raise ValidationError("Unsupported file type")

# User Model


class User(AbstractUser):
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


# Choices for music files as public/private/protected.
TYPE_CHOICES = [
    ('public', 'Public'),
    ('private', 'Private'),
    ('protected', 'Protected'),
]

# Music Model


class Musics(models.Model):
    title = models.CharField(max_length=255)
    music = models.FileField(
        validators=[ext_validator])
    category = models.CharField(
        max_length=10, choices=TYPE_CHOICES, blank=False)
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    email_addresses_with_access = models.TextField(
        blank=True, help_text="Comma-separated email addresses")

    def __str__(self):
        return self.title

    # Function so that if the user selects protected category the email_addresses with access can not be blank
    def clean(self):
        super().clean()
        if self.category == 'protected' and not self.email_addresses_with_access:
            raise ValidationError(
                {'email_addresses_with_access': 'Email addresses cannot be blank for protected category.'})
