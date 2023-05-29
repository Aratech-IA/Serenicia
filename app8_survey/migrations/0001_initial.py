# Generated by Django 3.2.13 on 2023-04-02 16:00

import app8_survey.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app4_ehpad_base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Order')),
                ('title', models.CharField(max_length=200)),
                ('can_comment', models.BooleanField(default=True, verbose_name='Can add comment')),
                ('comment_title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Comment title')),
            ],
            options={
                'verbose_name': 'Chapter',
                'ordering': ['number'],
            },
        ),
        migrations.CreateModel(
            name='Notation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app8_survey.chapter')),
            ],
        ),
        migrations.CreateModel(
            name='NotationChoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], verbose_name='Value')),
                ('text', models.CharField(max_length=50, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Notation',
                'ordering': ['value'],
                'unique_together': {('value', 'text')},
            },
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('satisfaction', 'Satisfaction'), ('other', 'Other')], max_length=15, verbose_name='Survey type')),
                ('target', models.CharField(choices=[('family', 'Family'), ('resident', 'Resident'), ('employees', 'Employees'), ('referents', 'Referents')], max_length=20, verbose_name='Target')),
                ('title', models.CharField(blank=True, max_length=200, null=True, verbose_name='Title')),
                ('year', models.PositiveIntegerField(default=app8_survey.models.get_year, verbose_name='Year')),
                ('intro', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Introduction')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is active')),
                ('chapters', models.ManyToManyField(blank=True, to='app8_survey.Chapter', verbose_name='Chapters')),
                ('created_by', models.ForeignKey(limit_choices_to=models.Q(('user__groups__permissions__codename', 'view_monavis'), ('user__is_active', True)), on_delete=django.db.models.deletion.CASCADE, to='app4_ehpad_base.profileserenicia', verbose_name='Created by')),
            ],
            options={
                'verbose_name': 'Survey',
            },
        ),
        migrations.CreateModel(
            name='SurveyResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filling_date', models.DateField(blank=True, null=True)),
                ('last_update', models.DateTimeField(blank=True, null=True)),
                ('interviewee', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app4_ehpad_base.profileserenicia')),
                ('notation', models.ManyToManyField(blank=True, to='app8_survey.Notation')),
                ('survey', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='app8_survey.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Order')),
                ('text', models.CharField(max_length=200)),
                ('notation_choices', models.ManyToManyField(to='app8_survey.NotationChoices', verbose_name='Possible answers')),
            ],
            options={
                'verbose_name': 'Question',
                'ordering': ['number'],
            },
        ),
        migrations.AddField(
            model_name='notation',
            name='notation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app8_survey.notationchoices'),
        ),
        migrations.AddField(
            model_name='notation',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app8_survey.question'),
        ),
        migrations.AddField(
            model_name='chapter',
            name='questions',
            field=models.ManyToManyField(blank=True, to='app8_survey.Question', verbose_name='Questions'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=2000, null=True)),
                ('chapter', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app8_survey.chapter')),
                ('surveyresponse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app8_survey.surveyresponse')),
            ],
            options={
                'unique_together': {('chapter', 'surveyresponse')},
            },
        ),
    ]