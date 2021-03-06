# Generated by Django 3.2.8 on 2021-11-01 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='desc',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='image',
            field=models.ImageField(default=0, upload_to='pics'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='data',
            name='title',
            field=models.TextField(default=0),
            preserve_default=False,
        ),

    ]
