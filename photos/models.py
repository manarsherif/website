from __future__ import unicode_literals
from django.db import models
#from django.core.files.storage import FileSystemStorage
# Create your models here.
#fs = FileSystemStorage(location='/media/photos')


class Photo(models.Model):
    name        =   models.CharField(max_length=255)
    photo       =   models.ImageField(upload_to= '/home/asmaanabil/github/website/photos/media/photos/')
    features    =   models.FileField(blank = True , upload_to= '/home/asmaanabil/github/website/photos/media/features/')

    def __str__(self):
        return self.name

