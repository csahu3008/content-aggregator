# Generated by Django 2.2.3 on 2019-07-15 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190710_1058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-date_published'], 'verbose_name_plural': 'News'},
        ),
    ]
