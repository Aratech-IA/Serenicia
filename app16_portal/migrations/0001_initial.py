# Generated by Django 3.2.13 on 2023-04-02 16:02

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import secrets


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Group',
            },
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_public', models.BooleanField(default=True)),
                ('is_local', models.BooleanField(default=False)),
                ('key', models.CharField(max_length=1800)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('url', models.CharField(max_length=200, unique=True, validators=[django.core.validators.RegexValidator('https://', 'Your URL must start by "https://"')], verbose_name='URL')),
                ('facebook', models.CharField(blank=True, help_text='auto completion', max_length=200, null=True, verbose_name='Facebook')),
                ('main_site', models.CharField(blank=True, help_text='auto completion', max_length=200, null=True, verbose_name='Main site')),
                ('is_linked', models.BooleanField(default=False, help_text='The site know the portal public key, auto completion', verbose_name='Is linked')),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app16_portal.group', verbose_name='Group')),
                ('public_key', models.ForeignKey(blank=True, help_text='auto completion', null=True, on_delete=django.db.models.deletion.CASCADE, to='app16_portal.key', verbose_name='Public key')),
            ],
            options={
                'verbose_name': 'Site',
            },
        ),
        migrations.CreateModel(
            name='PortalProfile',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('key', models.CharField(default=secrets.token_urlsafe, max_length=100, verbose_name='Connexion key')),
                ('linked_sites', models.ManyToManyField(to='app16_portal.Site')),
                ('site_group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app16_portal.group', verbose_name='Site group')),
            ],
            options={
                'verbose_name': 'Portal profile',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AddConstraint(
            model_name='key',
            constraint=models.UniqueConstraint(condition=models.Q(('is_public', False)), fields=('is_public',), name='private_key'),
        ),
        migrations.AddConstraint(
            model_name='key',
            constraint=models.UniqueConstraint(condition=models.Q(('is_local', True), ('is_public', True)), fields=('is_public', 'is_local'), name='local_public_key'),
        ),
    ]
