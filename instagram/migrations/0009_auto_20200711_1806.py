# Generated by Django 3.0.7 on 2020-07-11 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instagram', '0008_auto_20200708_2215'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ManyToManyField(blank=True, to='instagram.tag'),
        ),
    ]
