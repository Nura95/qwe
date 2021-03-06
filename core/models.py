from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.


class Signal(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    data = JSONField()
    def __str__(self):
        return self.name


class File(models.Model):
    file = models.FileField(upload_to='item_files')
    time_created = models.DateTimeField(auto_now_add=True)

