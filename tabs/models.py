from django.db import models

# Create your models here.
class activities(models.Model):
    title = models.TextField(verbose_name='title')
    announced_date = models.TextField(verbose_name='applicant')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'activities'
        verbose_name = 'Activities'
        verbose_name_plural = 'Activities'

class award(models.Model):
    title = models.TextField(verbose_name='title')
    content = models.TextField(verbose_name='content')
    date = models.TextField(verbose_name='date')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'award'
        verbose_name = 'Award'
        verbose_name_plural = 'Award'

class Conference(models.Model):
    title = models.TextField(verbose_name='title')
    content = models.TextField(verbose_name='content')
    academic_conference = models.TextField(verbose_name='academic_conference')
    period = models.TextField(verbose_name='period')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'conference'
        verbose_name = 'Conference'
        verbose_name_plural = 'Conference'