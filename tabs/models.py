from django.db import models

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