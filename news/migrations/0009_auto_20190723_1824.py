# Generated by Django 2.2.3 on 2019-07-23 12:24

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0008_auto_20190719_0843'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='like',
        ),
        migrations.AddField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]