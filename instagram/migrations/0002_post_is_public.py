# Generated by Django 3.0.7 on 2020-07-01 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='공게여부'),
        ),
    ]
