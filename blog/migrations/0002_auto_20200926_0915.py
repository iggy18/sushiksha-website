# Generated by Django 3.1.1 on 2020-09-26 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail',
            field=models.ImageField(upload_to='blog-post-thumbnail'),
        ),
    ]
