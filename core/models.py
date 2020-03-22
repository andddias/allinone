from django.db import models


class MyModel(models.Model):
    upload = models.FileField(upload_to='uploads/', blank=True)

    class Meta:
        verbose_name = ''
        verbose_name_plural = ''

    def __str__(self):
        return self.upload
