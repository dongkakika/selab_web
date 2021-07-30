from django.db import models

# Create your models here.
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