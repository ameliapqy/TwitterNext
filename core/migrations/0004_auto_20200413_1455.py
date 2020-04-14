# Generated by Django 3.0.5 on 2020-04-13 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200412_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hashtag',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='hashtag',
            name='user',
        ),
        migrations.AddField(
            model_name='hashtag',
            name='tweets',
            field=models.ManyToManyField(to='core.Tweet'),
        ),
        migrations.AlterField(
            model_name='hashtag',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='body',
            field=models.CharField(max_length=280),
        ),
    ]