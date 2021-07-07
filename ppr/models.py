from django.db import models
from django.conf import settings

# Create your models here.
class ip(models.Model):
    title = models.TextField(verbose_name='title')
    type = models.TextField(verbose_name='type', null=True, blank=True)
    applicant = models.TextField(verbose_name='applicant')
    date = models.TextField(verbose_name='applicant')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ip'
        verbose_name = 'Intellectual Property'
        verbose_name_plural = 'Intellectual Property'

class rp(models.Model):
    title = models.TextField(verbose_name='title')
    org = models.TextField(verbose_name='org', null=True, blank=True)
    period = models.TextField(verbose_name='period')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'rp'
        verbose_name = 'Research & Project'
        verbose_name_plural = 'Research & Project'

class People(models.Model):
    name = models.TextField(verbose_name='name')
    content = models.TextField(verbose_name='content')
    email = models.TextField(verbose_name='email')
    img_upload = models.ImageField(
        blank=True,  # 비어도 ok
        null = True, # null ok
        upload_to="image/" # 경로 설정
    )

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'people'
        verbose_name = 'People'
        verbose_name_plural = 'People'

class Staff(models.Model):
    name = models.TextField(verbose_name='name')
    content = models.TextField(verbose_name='content')
    email = models.TextField(verbose_name='email')
    img_upload = models.ImageField(
        blank=True,  # 비어도 ok
        null = True, # null ok
        upload_to="image/" # 경로 설정
    )

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'staff'
        verbose_name = 'Staff'
        verbose_name_plural = 'Staff'

class Professor(models.Model):
    content = models.TextField(verbose_name='content')

    def __str__(self):
        return self.content

    class Meta:
        db_table = 'professor'
        verbose_name = 'professor'
        verbose_name_plural = 'professor'

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

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'research'
        verbose_name = 'Research'
        verbose_name_plural = 'Research'

