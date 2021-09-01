# Generated by Django 2.2.17 on 2021-08-31 21:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('userid', models.CharField(max_length=20, unique=True, verbose_name='ID')),
                ('password', models.CharField(max_length=256, verbose_name='PW')),
                ('email', models.EmailField(max_length=128, null=True, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=50, null=True, verbose_name='username')),
                ('level', models.CharField(choices=[('3', 'Lv3_Intern Staff'), ('2', 'Lv2_Internal Member'), ('1', 'Lv1_Manager'), ('0', 'Lv0_Developer')], default=3, max_length=18, verbose_name='level')),
                ('auth', models.CharField(max_length=10, null=True, verbose_name='auth')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True, verbose_name='date_joined')),
                ('activate', models.BooleanField(default=False, verbose_name='activate')),
                ('is_active', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'db_table': 'user',
            },
        ),
    ]
