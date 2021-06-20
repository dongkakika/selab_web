from django.db import models

# Create your models here.
class People(models.Model):
    content = models.TextField(verbose_name='content')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'people'
        verbose_name = 'People'
        verbose_name_plural = 'People'