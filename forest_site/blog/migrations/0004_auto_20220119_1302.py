# Generated by Django 3.1.4 on 2022-01-19 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210610_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='forest-of-spruce.jpg', null=True, upload_to='uploaded_images', verbose_name='image'),
        ),
    ]
