# Generated by Django 2.2.3 on 2019-07-25 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0011_auto_20190723_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='author',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='picture',
            field=models.ImageField(default='images/default.jpg', max_length=400, upload_to='images/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='url_image',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
