# Generated by Django 2.2.17 on 2021-10-15 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='activities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
                ('announced_date', models.TextField(verbose_name='announced_date')),
            ],
            options={
                'verbose_name': 'Activities',
                'verbose_name_plural': 'Activities',
                'db_table': 'activities',
            },
        ),
        migrations.CreateModel(
            name='award',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('date', models.TextField(verbose_name='date')),
            ],
            options={
                'verbose_name': 'Award',
                'verbose_name_plural': 'Award',
                'db_table': 'award',
            },
        ),
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
                ('academic_conference', models.TextField(verbose_name='academic_conference')),
                ('period', models.TextField(verbose_name='period')),
            ],
            options={
                'verbose_name': 'Conference',
                'verbose_name_plural': 'Conference',
                'db_table': 'conference',
            },
        ),
        migrations.CreateModel(
            name='Etc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
                ('content', models.TextField(verbose_name='content')),
                ('date', models.TextField(verbose_name='date')),
            ],
            options={
                'verbose_name': 'Etc',
                'verbose_name_plural': 'Etc',
                'db_table': 'etc',
            },
        ),
        migrations.CreateModel(
            name='ip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
                ('type', models.TextField(blank=True, null=True, verbose_name='type')),
                ('number', models.TextField(verbose_name='number')),
                ('date', models.TextField(verbose_name='date')),
            ],
            options={
                'verbose_name': 'Intellectual Property',
                'verbose_name_plural': 'Intellectual Property',
                'db_table': 'ip',
            },
        ),
        migrations.CreateModel(
            name='rp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='title')),
                ('org', models.TextField(blank=True, null=True, verbose_name='org')),
                ('period', models.TextField(verbose_name='period')),
            ],
            options={
                'verbose_name': 'Research & Project',
                'verbose_name_plural': 'Research & Project',
                'db_table': 'rp',
            },
        ),
    ]
