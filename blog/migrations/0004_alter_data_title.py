# Generated by Django 3.2.8 on 2021-11-01 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='title',
            field=models.TextField(),
        ),
    ]
