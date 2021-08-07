from django.db import models

# Create your models here.
class Gallery(models.Model):
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
        db_table = 'gallery'
        verbose_name = 'Gallery'
        verbose_name_plural = 'Gallery'