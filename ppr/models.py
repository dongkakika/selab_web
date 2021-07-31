from django.db import models
from django.conf import settings

# Create your models here.


class Journal(models.Model):
    title = models.CharField(max_length=128, verbose_name='title')
    journals = models.TextField(verbose_name='journals')
    issued_date = models.TextField(verbose_name='issued_date')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'journal'
        verbose_name = 'Journal'
        verbose_name_plural = 'Journal'

class Publication(models.Model):
    title = models.CharField(max_length=128, verbose_name='title')
    publisher = models.TextField(verbose_name='publisher')
    published_date = models.TextField(verbose_name='published_date')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'publication'
        verbose_name = 'Publication'
        verbose_name_plural = 'Publication'


class Research(models.Model):
    title = models.TextField(verbose_name='title', null=True, blank=True)
    img = models.ImageField(
        blank=True,  # 비어도 ok
        null=True,  # null ok
        upload_to="image/"  # 경로 설정
    )
    content = models.TextField(verbose_name='content')
    left_right_check = models.BooleanField(verbose_name='left_right_check')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'research'
        verbose_name = 'Research'
        verbose_name_plural = 'Research'

