# Generated by Django 2.2.6 on 2019-10-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='dept_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='role',
            field=models.CharField(default='Student', max_length=30),
        ),
    ]
