# Generated by Django 2.2.3 on 2019-07-23 13:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0009_auto_20190723_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='likes',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
    ]